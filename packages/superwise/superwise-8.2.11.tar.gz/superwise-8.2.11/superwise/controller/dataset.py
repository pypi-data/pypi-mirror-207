""" This module implement dataset functionality  """
import os
import tempfile
import time
import urllib.parse
from typing import List
from typing import Union

import pandas as pd
from requests import ReadTimeout

from superwise.controller.base import BaseController
from superwise.models.dataset import Dataset
from superwise.resources.superwise_enums import DatasetOnFailureOptions
from superwise.resources.superwise_enums import DatasetStatus
from superwise.utils.exceptions import SuperwiseDatasetFailureError
from superwise.utils.exceptions import SuperwiseTimeoutError
from superwise.utils.storage import validate_files_size
from superwise.utils.storage.azure_storage import AzureClientReader
from superwise.utils.storage.dataframe import dataframe_to_tempfile
from superwise.utils.storage.gcs import GcsClient
from superwise.utils.storage.local import load_from_local_storage
from superwise.utils.storage.s3 import S3Client


def create_file_from_dataframe(dataset: Dataset, dataframe: pd.DataFrame):
    tf = tempfile.NamedTemporaryFile(prefix=f"{dataset.name}_from_dataframe", suffix="parquet")


class DatasetController(BaseController):
    """Datasets controller class, implement functionalities for dataset API"""

    def __init__(self, client, sw, internal_bucket):
        """

        ### Args:

        `client`: superwise client object

        `sw`: superwise object

        """
        super().__init__(client, sw)
        self.path = "model/v1/datasets"
        self.model_name = "Dataset"
        self._internal_bucket = internal_bucket
        self._scheme_to_func = {
            "gs": self._get_file_from_gcs,
            "s3": self._get_file_from_s3,
            "abfs": self._get_file_from_blob_storage,
        }

    @staticmethod
    def _get_file_from_gcs(file_path, service_account, validate_size, **kwargs) -> dict:
        gcs = GcsClient()
        return gcs.get_file_from_gcs(file_path=file_path, service_account=service_account, validate_size=validate_size)

    @staticmethod
    def _get_file_from_s3(file_path, access_key_id, secret_access_key, role_arn, validate_size, **kwargs) -> dict:
        s3_client = S3Client()
        return s3_client.get_s3_file(
            file_path=file_path,
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            role_arn=role_arn,
            validate_size=validate_size,
        )

    @staticmethod
    def _get_file_from_blob_storage(file_path, connection_string, validate_size, **kwargs) -> dict:
        azure_client = AzureClientReader(connection_string=connection_string)
        return azure_client.get_file_from_blob_storage(file_path=file_path, validate_size=validate_size)

    def _upload_files_to_storage(
        self,
        file_paths: Union[str, List[str]],
        project_id: int,
        gcs_service_account: str = None,
        aws_access_key_id: str = None,
        aws_secret_access_key: str = None,
        aws_role_arn: str = None,
        azure_connection_string: str = None,
    ):
        auth_params = dict(
            service_account=gcs_service_account,
            access_key_id=aws_access_key_id,
            secret_access_key=aws_secret_access_key,
            role_arn=aws_role_arn,
            connection_string=azure_connection_string,
        )
        total_size = 0
        for i, file_path in enumerate(file_paths):
            external_path = file_path
            parsed_url = urllib.parse.urlparse(file_path)
            storage_scheme = parsed_url.scheme

            if storage_scheme in self._scheme_to_func:
                get_file_func = self._scheme_to_func[storage_scheme]
                file = get_file_func(file_path, validate_size=True, **auth_params)
            else:
                file = load_from_local_storage(file_path, validate_size=True)
                external_path = f"file://{file['filename']}"
            total_size += file["size"]
            validate_files_size(filenames=file_paths[: i + 1], size=total_size)

            base_name, extension = os.path.splitext(file["filename"])
            file_name = self._internal_bucket.generate_file_name(prefix=base_name, extension=extension)
            blob_path = f"datasets/project_id={project_id}/{file_name}"
            inner_path = self._internal_bucket.upload(blob_path=blob_path, content=file["data"])
            yield inner_path, external_path

    @staticmethod
    def _extract_inner_paths(file_paths: List[tuple]) -> List[str]:
        return [file_path[0] for file_path in file_paths]

    @staticmethod
    def _extract_external_paths(file_paths: List[tuple]) -> List[str]:
        return [file_path[1] for file_path in file_paths]

    def _get_field(self, dataset_id, field):
        dataset = self.get_by_id(idx=dataset_id)

        return getattr(dataset, field)

    def _get_timeout_func(self, dataset_id, dataset_statuses: List[DatasetStatus], timeout_seconds=30):
        _started_at = time.perf_counter()

        def __wait_to_status():
            dataset = self.get_by_id(dataset_id)
            status = dataset.status
            _time_since_start = time.perf_counter() - _started_at
            while status not in [dataset_status.value for dataset_status in dataset_statuses]:
                if _time_since_start > timeout_seconds:
                    raise SuperwiseTimeoutError(
                        f"Timed out while waiting for dataset with ID: '{dataset_id}' to be in one of "
                        f"the statuses {[s.value for s in dataset_statuses]}, "
                        f"got status: '{self._get_field(dataset_id, 'status')}', "
                        f"with reason: '{self._get_field(dataset_id, 'status_reason') or '<unknown reason>'}'"
                    )
                try:
                    dataset = self.get_by_id(dataset_id, timeout=10)
                    status = dataset.status
                except ReadTimeout:
                    self.logger.exception(f"Request for getting dataset:{dataset_id} timed out")
                time.sleep(5)
                _time_since_start = time.perf_counter() - _started_at

            return dataset

        return __wait_to_status

    def _trigger_full_flow(
        self,
        model: Dataset,
        return_model: bool,
        wait_until_complete: bool,
        timeout_seconds: int,
        on_failure: DatasetOnFailureOptions,
        **kwargs,
    ):
        model.full_flow = True
        if model._from_dataframe:
            os.remove(model._tempfile_path)
            del model._from_dataframe
            del model._tempfile_path

        response = BaseController.create(self, model, return_model, **kwargs)
        response_id = response.id if return_model else response["id"]

        if not wait_until_complete:
            return response

        wait_to_status = self._get_timeout_func(
            timeout_seconds=timeout_seconds,
            dataset_id=response_id,
            dataset_statuses=[DatasetStatus.SUMMARIZED, DatasetStatus.FAILED],
        )
        try:
            self.logger.info("Waiting for the dataset to be completely processed...")
            dataset = wait_to_status()
        except SuperwiseTimeoutError:
            if on_failure == DatasetOnFailureOptions.RAISE:
                raise
            return response
        if dataset.status == DatasetStatus.FAILED.value and on_failure == DatasetOnFailureOptions.RAISE:
            raise SuperwiseDatasetFailureError(
                f"Dataset creation failed for ID '{response_id}'. "
                f"got status: '{self._get_field(response_id, 'status')}', "
                f"with reason: '{self._get_field(response_id, 'status_reason') or '<unknown reason>'}'"
            )

        return dataset

    def create(
        self,
        model: Dataset,
        return_model=True,
        gcs_service_account: dict = None,
        aws_access_key_id: str = None,
        aws_secret_access_key: str = None,
        aws_role_arn: str = None,
        azure_connection_string: str = None,
        wait_until_complete: bool = True,
        timeout_seconds: int = 60 * 5,
        on_failure="raise",
        **kwargs,
    ):
        """
        ### Description:

        Create a new dataset.

        ### Args:

        `model`: Dataset model.

        `return_model`: return model if True or response.body if False. Default True.

        `gcs_service_account`: GCP service account object used to authenticate and pull dataset files from a customer
                               GCS bucket. If not provided, will be inferred from the environment.
                               (See Google Cloud auth)

        `aws_access_key_id`: AWS access key ID used to authenticate and pull dataset files from a customer S3 bucket.
                             If not provided, will be inferred from the environment.
                             (Used together with `aws_secret_access_key` parameter)

        `aws_secret_access_key`: AWS secret access key used to authenticate and pull dataset files from a customer S3
                                 bucket. If not provided, will be inferred from the environment.
                                 (Used together with `aws_access_key_id` parameter)

        `aws_role_arn`: AWS role ARN used to authenticate and pull dataset files from a customer S3 bucket.
                        If not provided, the authentication will use the `aws_access_key_id` and `aws_secret_access_key`
                        parameters.

        `azure_connection_string`: Azure blob storage connection string used to authenticate and pull dataset files from
                                   a customer blob storage container.
                                   MUST be provided in order to pull files from azure.

        `wait_until_complete`: if True, wait until the dataset is fully processed in the system, and return the final
                               object. If False, return immediately after the dataset is created and the given dataset
                               files are validated, without waiting for the processing. A partially set Dataset object
                               is returned, without all the processed fields. Afterwards the status can be checked with
                               'get_by_id' method. Default True.

        `timeout_seconds`: Timeout for dataset processing waiting. Only relevant if 'wait_until_complete' is True.
                           Default 5 minutes.

        `on_failure`: Action to take in case the dataset processing failed. Only relevant if 'wait_until_complete'
                      is True. Possible values are:
                      - 'ignore': Don't raise an exception, and return the object.
                      - 'raise': Raise a 'SuperwiseDatasetFailureError' exception.
                      Default 'raise'.
        """
        if not isinstance(model.files, list):
            model.files = [model.files]
        on_failure = DatasetOnFailureOptions(on_failure)

        self.logger.info("Uploading dataset files...")
        file_paths = list(
            self._upload_files_to_storage(
                file_paths=model.files,
                project_id=model.project_id,
                gcs_service_account=gcs_service_account,
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                aws_role_arn=aws_role_arn,
                azure_connection_string=azure_connection_string,
            )
        )
        model.internal_files = self._extract_inner_paths(file_paths)
        model.files = self._extract_external_paths(file_paths)

        self.logger.info("Finished uploading, start processing dataset...")
        return self._trigger_full_flow(model, return_model, wait_until_complete, timeout_seconds, on_failure, **kwargs)
