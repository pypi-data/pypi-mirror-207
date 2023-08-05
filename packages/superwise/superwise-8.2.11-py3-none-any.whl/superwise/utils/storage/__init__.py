from typing import Union

import humanize

from superwise.config import Config
from superwise.utils.exceptions import SuperwiseFileTooLargeError


def extract_directory(url: str):
    """
    ### Description:

    extract  given url of gcs to bucket name and prefix

    ### Args:

    `url`:  the url to extract

    ### Return:

    a tuple of bucket and prefix
    """
    bucket = url.split("/")[2]
    prefix = "/".join(url.split("/")[3:])
    return bucket, prefix


def validate_file_size(file_path, file_size):
    if file_size > Config.FILE_SIZE_LIMIT_BYTES + Config.FILE_SIZE_PADDING:
        readable_file_size = humanize.filesize.naturalsize(file_size)
        readable_maximum_size = humanize.filesize.naturalsize(Config.FILE_SIZE_LIMIT_BYTES)
        raise SuperwiseFileTooLargeError(
            f"File '{file_path}' is too large: ({readable_file_size}), maximum size allowed is {readable_maximum_size}"
        )


def validate_files_size(filenames: Union[list, str], size: int):
    if not isinstance(filenames, list):
        filenames = [filenames]

    if size > Config.FILE_SIZE_LIMIT_BYTES + Config.FILE_SIZE_PADDING:
        readable_size = humanize.filesize.naturalsize(size)
        readable_maximum_size = humanize.filesize.naturalsize(Config.FILE_SIZE_LIMIT_BYTES)
        raise SuperwiseFileTooLargeError(
            f"The *total* size of the files: {filenames} is too large: ({readable_size}), "
            f"maximum size allowed is {readable_maximum_size}"
        )
