""" Tests src/tools/utils.py
"""
# type hints
import pathlib

# test
import pytest

# module to test
from tools.utils import manual_root, git_root


@pytest.fixture(name="manual")
def fixture_manual() -> pathlib.Path:
    """Instantiates manual_root function. 
    """
    return manual_root


@pytest.fixture(name="git")
def fixture_git() -> pathlib.Path:
    """Instantiates git_root function. 
    """
    return git_root


def test_manual_root(manual: pathlib.Path) -> None:
    """Tests if manual_root returns pathlib.Path object.
    """
    assert isinstance(manual(__name__),
                      (pathlib.WindowsPath, pathlib.PosixPath))


def test_manual_root_raise(manual: pathlib.Path) -> None:
    """Tests if manual_root returns IndexError.
    """
    with pytest.raises(IndexError):
        manual(__name__, num_parent=10)


def test_git_root(git: pathlib.Path) -> None:
    """Tests if git_root returns pathlib.Path object.
    """
    assert isinstance(git(),
                      (pathlib.WindowsPath, pathlib.PosixPath))
