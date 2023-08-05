# -*- coding: utf-8 -*-

__all__ = (
    # exceptions
    "NotAFileError",
    "DirectoryNotFoundError",
    # path utils
    "check_if_path_exists",
    "check_if_file_exists",
    "check_if_dir_exists",
    "get_paths",
    "get_file_paths",
    "get_dir_paths",
    # type aliases
    "StrPath",
)

from kaparoo.filesystem.exceptions import DirectoryNotFoundError, NotAFileError
from kaparoo.filesystem.path import (
    check_if_dir_exists,
    check_if_file_exists,
    check_if_path_exists,
    get_dir_paths,
    get_file_paths,
    get_paths,
)
from kaparoo.filesystem.types import StrPath
