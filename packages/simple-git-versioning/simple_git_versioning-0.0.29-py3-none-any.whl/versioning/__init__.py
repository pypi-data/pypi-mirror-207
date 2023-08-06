# SPDX-License-Identifier: MIT

import os
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as importlib_metadata_version
from pathlib import Path
from typing import Iterator, Tuple

from packaging.version import Version
from sh import ErrorReturnCode, pushd
from sh.contrib import git


def _last() -> Version:
    """
    Return the last version explicitly set with a tag in the history
    """
    return Version(git.describe("--abbrev=0"))


def _patch(version: Version) -> Version:
    return Version(f"{version.major}.{version.minor}.{version.micro + 1}")


def _minor(version: Version) -> Version:
    return Version(f"{version.major}.{version.minor + 1}.0")


def _major(version: Version) -> Version:
    return Version(f"{version.major + 1}.0.0")


def _trailers(commit: str, *args: str) -> Iterator[Tuple[str, str]]:
    for trailer in (
        git(
            "interpret-trailers",
            "--no-divider",
            "--unfold",
            "--trim-empty",
            "--only-trailers",
            *args,
            _in=git.show("--format=format:%B", "--no-patch", commit),
        )
        .strip()
        .split("\n")
    ):
        key, value = trailer.split(":", maxsplit=1)
        yield key.strip(), value.strip()


def _is_git_work_tree() -> bool:
    """
    Return True if the current directory inside a git work tree, False otherwise
    """
    try:
        return git("rev-parse", "--is-inside-work-tree").strip() == "true"
    except ErrorReturnCode as exc:
        if exc.exit_code != 128:
            raise
        return False


def _version() -> Version:
    if not _is_git_work_tree():
        raise RuntimeError(f"{os.getcwd()} is not a git work tree")

    try:
        version = last = _last()
    except ErrorReturnCode as exc:
        if exc.exit_code != 128:
            raise
        return Version("0.0.0")
    for commit in git.log("--reverse", "--format=format:%H", f"{last}..")[:-1].split():
        for token, value in _trailers(
            commit, "--if-missing", "add", "--if-exists", "doNothing", "--trailer", "ci-version-bump: patch"
        ):
            if token != "ci-version-bump":
                continue

            if value == "patch":
                version = _patch(version)
            elif value == "minor":
                version = _minor(version)
            elif value == "major":
                version = _major(version)
            else:
                raise RuntimeError(
                    f"Unexpected value for ci-version-bump trailer: '{value}', expected one of patch, minor, or major"
                )
    return version


def version(project: Path = Path(".")) -> Version:
    """
    Compute the current version of a project based on git tags and git trailers
    """
    with pushd(project):
        return _version()


try:
    __version__ = importlib_metadata_version("simple-git-versioning")
except PackageNotFoundError:
    # package is not installed
    __version__ = str(version(Path(__file__).parent))
