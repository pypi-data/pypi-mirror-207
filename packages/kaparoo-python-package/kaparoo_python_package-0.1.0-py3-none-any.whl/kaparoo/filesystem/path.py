# -*- coding: utf-8 -*-

from __future__ import annotations

__all__ = (
    "check_if_path_exists",
    "check_if_file_exists",
    "check_if_dir_exists",
    "get_paths",
    "get_file_paths",
    "get_dir_paths",
)

import random
from collections.abc import Callable, Sequence
from pathlib import Path
from typing import TYPE_CHECKING, Literal, overload

from kaparoo.filesystem.exceptions import DirectoryNotFoundError, NotAFileError

if TYPE_CHECKING:
    from kaparoo.filesystem.types import StrPath


@overload
def check_if_path_exists(path: StrPath, *, stringify: Literal[False] = False) -> Path:
    ...


@overload
def check_if_path_exists(path: StrPath, *, stringify: Literal[True]) -> str:
    ...


@overload
def check_if_path_exists(path: StrPath, *, stringify: bool) -> Path | str:
    ...


def check_if_path_exists(path: StrPath, *, stringify: bool = False) -> Path | str:
    """Check if a given path exists and return it as a Path object.

    Args:
        path (StrPath): The path to check for existence.
        stringify (bool, optional): Whether to return the path as a string instead of a
            Path object. Defaults to False.

    Returns:
        The path as a Path object or a string, depending on the value of `stringify`.

    Raises:
        FileNotFoundError: If the path does not exist.
    """

    if not (path := Path(path)).exists():
        raise FileNotFoundError(f"no such path: {path}")

    return str(path) if stringify else path


@overload
def check_if_file_exists(path: StrPath, *, stringify: Literal[False] = False) -> Path:
    ...


@overload
def check_if_file_exists(path: StrPath, *, stringify: Literal[True]) -> str:
    ...


@overload
def check_if_file_exists(path: StrPath, *, stringify: bool) -> Path | str:
    ...


def check_if_file_exists(path: StrPath, *, stringify: bool = False) -> Path | str:
    """Check if a given path exists and is a file, and return it as a Path object.

    Args:
        path (StrPath): The file path to check for existence.
        stringify (bool, optional): Whether to return the path as a string instead of a
            Path object. Defaults to False.

    Returns:
        The path as a Path object or a string, depending on the value of `stringify`.

    Raises:
        FileNotFoundError: If the path does not exist.
        NotAFileError: If the path exists but is not a file.
    """

    if not (path := Path(path)).exists():
        raise FileNotFoundError(f"no such file: {path}")
    elif not path.is_file():
        raise NotAFileError(f"not a file: {path}")

    return str(path) if stringify else path


@overload
def check_if_dir_exists(path: StrPath, *, stringify: Literal[False] = False) -> Path:
    ...


@overload
def check_if_dir_exists(path: StrPath, *, stringify: Literal[True]) -> str:
    ...


@overload
def check_if_dir_exists(path: StrPath, *, stringify: bool) -> Path | str:
    ...


def check_if_dir_exists(
    path: StrPath, *, make: bool | int = False, stringify: bool = False
) -> Path | str:
    """Check if a given path exists and is a directory, and return it as a Path object.

    Args:
        path (StrPath): The directory path to check for existence.
        make (bool|int, optional): Whether to create the directory if it does not exist.
            If an int is provided, use it as the octal mode for the directory.
            Defaults to False.
        stringify (bool, optional): Whether to return the path as a string instead of a
            Path object. Defaults to False.

    Returns:
        The path as a Path object or a string, depending on the value of `stringify`.

    Raises:
        DirectoryNotFoundError: If the path does not exist and `make` is False.
            Note that `DirectoryNotFoundError` inherits from `FileNotFoundError`.
        NotADirectoryError: If the path exists but is not a directory.
    """

    if not (path := Path(path)).exists():
        if make is not False:
            path.mkdir(parents=True)
            if make is not True:  # `make` AS IS int
                path.chmod(mode=make)
        raise DirectoryNotFoundError(f"no such directory: {path}")
    elif not path.is_dir():
        raise NotADirectoryError(f"not a directory: {path}")

    return str(path) if stringify else path


@overload
def get_paths(
    root: StrPath,
    *,
    pattern: str | None = None,
    num_samples: int | None = None,
    ignores: Sequence[StrPath] | None = None,
    condition: Callable[[Path], bool] | None = None,
    stringify: Literal[False] = False,
) -> Sequence[Path]:
    ...


@overload
def get_paths(
    root: StrPath,
    *,
    pattern: str | None = None,
    num_samples: int | None = None,
    ignores: Sequence[StrPath] | None = None,
    condition: Callable[[Path], bool] | None = None,
    stringify: Literal[True],
) -> Sequence[str]:
    ...


@overload
def get_paths(
    root: StrPath,
    *,
    pattern: str | None = None,
    num_samples: int | None = None,
    ignores: Sequence[StrPath] | None = None,
    condition: Callable[[Path], bool] | None = None,
    stringify: bool,
) -> Sequence[Path] | Sequence[str]:
    ...


def get_paths(
    root: StrPath,
    *,
    pattern: str | None = None,
    num_samples: int | None = None,
    ignores: Sequence[StrPath] | None = None,
    condition: Callable[[Path], bool] | None = None,
    stringify: bool = False,
) -> Sequence[Path] | Sequence[str]:
    """Get paths of files or directories in a given directory.

    Args:
        root (StrPath): The directory to search for paths.
        pattern (str, optional): A glob pattern to match the paths against. Defaults to
            None and automatically uses "*" to list all paths included in the `root`.
        num_samples (int, optional): A maximum number of paths to return. If given and
            its value is smaller than the total number of paths, only the `num_samples`
            paths of the total are randomly selected and returned. Hence, even using the
            same `num_samples`, may return a different result. Defaults to None.
        ignores (Sequence[StrPath], optional): A sequence of paths to ignore. If any path
            in `ignores` does not start with `root`, it is treated as a relative path.
            For example, `any/path` is treated as `root/any/path`. Defaults to None.
        condition (Callable[[Path], bool], optional): A predicate that takes a Path object
            and decides whether to include the path in the results. Defaults to None.
        stringify (bool, optional): Whether to return a sequence of strings instead of a
            sequence of Path objects. Defaults to False.

    Returns:
        The paths that match the specified criteria as a sequence of Path objects or a
            sequence of strings, depending on the value of `stringify`.

    Raises:
        DirectoryNotFoundError: If `root` does not exist.
        NotADirectoryError: If `root` exists but is not a directory.
        FileNotFoundError: If no paths match the specified `pattern`.
        ValueError: If `num_samples` is not a positive int.
    """  # noqa: E501

    root = check_if_dir_exists(root)

    if not isinstance(pattern, str):
        pattern = "*"

    paths = [p for p in root.glob(pattern)]

    if callable(condition):
        paths = [p for p in paths if condition(p)]

    if not paths:
        raise FileNotFoundError(f'no path matches "{pattern}" at {root}')

    if not ignores:
        ignores = []

    for ignore in ignores:
        ignore_path = Path(ignore)
        if root not in ignore_path.parents:
            ignore_path = root / ignore_path

        if ignore_path in paths:
            paths.remove(ignore_path)

    if isinstance(num_samples, int) and num_samples < len(paths):
        if num_samples <= 0:
            raise ValueError("`num_samples` must be a positive int")
        paths = random.sample(paths, num_samples)

    return [str(p) for p in paths] if stringify else paths


@overload
def get_file_paths(
    root: StrPath,
    *,
    pattern: str | None = None,
    num_samples: int | None = None,
    ignores: Sequence[StrPath] | None = None,
    condition: Callable[[Path], bool] | None = None,
    stringify: Literal[False] = False,
) -> Sequence[Path]:
    ...


@overload
def get_file_paths(
    root: StrPath,
    *,
    pattern: str | None = None,
    num_samples: int | None = None,
    ignores: Sequence[StrPath] | None = None,
    condition: Callable[[Path], bool] | None = None,
    stringify: Literal[True],
) -> Sequence[str]:
    ...


@overload
def get_file_paths(
    root: StrPath,
    *,
    pattern: str | None = None,
    num_samples: int | None = None,
    ignores: Sequence[StrPath] | None = None,
    condition: Callable[[Path], bool] | None = None,
    stringify: bool,
) -> Sequence[Path] | Sequence[str]:
    ...


def get_file_paths(
    root: StrPath,
    *,
    pattern: str | None = None,
    num_samples: int | None = None,
    ignores: Sequence[StrPath] | None = None,
    condition: Callable[[Path], bool] | None = None,
    stringify: bool = False,
) -> Sequence[Path] | Sequence[str]:
    """Get paths of files in a given directory.

    Args:
        root (StrPath): The directory to search for paths.
        pattern (str, optional): A glob pattern to match the paths against. Defaults to
            None and automatically uses "*" to list all paths included in the `root`.
        num_samples (int, optional): A maximum number of paths to return. If given and
            its value is smaller than the total number of paths, only the `num_samples`
            paths of the total are randomly selected and returned. Hence, even using the
            same `num_samples`, may return a different result. Defaults to None.
        ignores (Sequence[StrPath], optional): A sequence of paths to ignore. If any path
            in `ignores` does not start with `root`, it is treated as a relative path.
            For example, `any/path` is treated as `root/any/path`. Defaults to None.
        condition (Callable[[Path], bool], optional): A predicate that takes a Path object
            and decides whether to include the path in the results. Defaults to None.
        stringify (bool, optional): Whether to return a sequence of strings instead of a
            sequence of Path objects. Defaults to False.

    Returns:
        The paths that match the specified criteria as a sequence of Path objects or a
            sequence of strings, depending on the value of `stringify`.

    Raises:
        DirectoryNotFoundError: If `root` does not exist.
        NotADirectoryError: If `root` exists but is not a directory.
        FileNotFoundError: If no paths match the specified `pattern`.
        ValueError: If `num_samples` is not a positive int.
    """  # noqa: E501

    if not callable(condition):
        file_condition = lambda p: p.is_file()  # noqa: E731
    else:
        file_condition = lambda p: p.is_file() and condition(p)  # type: ignore[misc] # noqa: E501, E731

    file_paths = get_paths(
        root,
        pattern=pattern,
        num_samples=num_samples,
        ignores=ignores,
        condition=file_condition,
        stringify=stringify,
    )

    return file_paths


@overload
def get_dir_paths(
    root: StrPath,
    *,
    pattern: str | None = None,
    num_samples: int | None = None,
    ignores: Sequence[StrPath] | None = None,
    condition: Callable[[Path], bool] | None = None,
    stringify: Literal[False] = False,
) -> Sequence[Path]:
    ...


@overload
def get_dir_paths(
    root: StrPath,
    *,
    pattern: str | None = None,
    num_samples: int | None = None,
    ignores: Sequence[StrPath] | None = None,
    condition: Callable[[Path], bool] | None = None,
    stringify: Literal[True],
) -> Sequence[str]:
    ...


@overload
def get_dir_paths(
    root: StrPath,
    *,
    pattern: str | None = None,
    num_samples: int | None = None,
    ignores: Sequence[StrPath] | None = None,
    condition: Callable[[Path], bool] | None = None,
    stringify: bool,
) -> Sequence[Path] | Sequence[str]:
    ...


def get_dir_paths(
    root: StrPath,
    *,
    pattern: str | None = None,
    num_samples: int | None = None,
    ignores: Sequence[StrPath] | None = None,
    condition: Callable[[Path], bool] | None = None,
    stringify: bool = False,
) -> Sequence[Path] | Sequence[str]:
    """Get paths of directories in a given directory.

    Args:
        root (StrPath): The directory to search for paths.
        pattern (str, optional): A glob pattern to match the paths against. Defaults to
            None and automatically uses "*" to list all paths included in the `root`.
        num_samples (int, optional): A maximum number of paths to return. If given and
            its value is smaller than the total number of paths, only the `num_samples`
            paths of the total are randomly selected and returned. Hence, even using the
            same `num_samples`, may return a different result. Defaults to None.
        ignores (Sequence[StrPath], optional): A sequence of paths to ignore. If any path
            in `ignores` does not start with `root`, it is treated as a relative path.
            For example, `any/path` is treated as `root/any/path`. Defaults to None.
        condition (Callable[[Path], bool], optional): A predicate that takes a Path object
            and decides whether to include the path in the results. Defaults to None.
        stringify (bool, optional): Whether to return a sequence of strings instead of a
            sequence of Path objects. Defaults to False.

    Returns:
        The paths that match the specified criteria as a sequence of Path objects or a
            sequence of strings, depending on the value of `stringify`.

    Raises:
        DirectoryNotFoundError: If `root` does not exist.
        NotADirectoryError: If `root` exists but is not a directory.
        FileNotFoundError: If no paths match the specified `pattern`.
        ValueError: If `num_samples` is not a positive int.
    """  # noqa: E501

    if not callable(condition):
        dir_condition = lambda p: p.is_dir()  # noqa: E731
    else:
        dir_condition = lambda p: p.is_dir() and condition(p)  # type: ignore[misc] # noqa: E501, E731

    dir_paths = get_paths(
        root,
        pattern=pattern,
        num_samples=num_samples,
        ignores=ignores,
        condition=dir_condition,
        stringify=stringify,
    )

    return dir_paths
