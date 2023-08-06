import os
import platform
from pathlib import Path


def get_creation_time(file_path: os.PathLike) -> float | int:
    if platform.system() == "Windows":
        return os.path.getctime(file_path)
    else:
        stat = os.stat(file_path)
        try:
            return stat.st_birthtime
        except AttributeError:
            return stat.st_ctime


def find_last_added_file(
    dir_path: os.PathLike,
    glob_pattern: str | None = None,
    recursive: bool = False,
    regex_pattern: str | None = None,
) -> Path:
    """
    Find the last added file in a directory.

    :param dir_path: Path to the directory to search in.
    :param glob_pattern: Glob pattern to match files.
    :param recursive: Search recursively.
    :return: Path to the last added file.
    """
    dir_path = Path(dir_path)
    if glob_pattern is None:
        files = dir_path.iterdir()
    else:
        if recursive:
            files = dir_path.rglob(glob_pattern)
        else:
            files = dir_path.glob(glob_pattern)

    if regex_pattern is not None:
        import re

        files = filter(lambda f: re.search(regex_pattern, f.name), files)
    try:
        last_added_file = max(files, key=get_creation_time)
        return last_added_file
    except:
        raise ValueError(
            f"No files found in {dir_path} with pattern {glob_pattern} (recursive={recursive})"
        )
