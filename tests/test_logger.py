""" Tests src/tools/logger.py
"""
# type hints
import pathlib
import logging

# test
import pytest

# module to test
from tools.logger import LoggerAttrib, get_logger, close_logger


@pytest.fixture(name="logger_att")
def fixture_logger_att() -> LoggerAttrib:
    """Instantiates LoggerAttrib object. 
    """
    return LoggerAttrib(__name__, num_parent=1)


@pytest.fixture(name="logger")
def fixture_logger(logger_att) -> logging.Logger:
    """Instantiates logging.Logger object. 
    """
    return get_logger(logger_att)


def test_logs_path(logger_att: LoggerAttrib) -> None:
    """Tests if logs_path is a path.
    """
    assert isinstance(logger_att.logs_path(),
                      (pathlib.WindowsPath, pathlib.PosixPath))


def test_file_handler(logger_att: LoggerAttrib) -> None:
    """Tests if logger_att.file_handler returns logging.FileHandler object.
    """
    assert isinstance(logger_att.file_handler(), logging.FileHandler)


def test_stream_handler(logger_att: LoggerAttrib) -> None:
    """Tests if logger_att.file_handler returns logging.StreamHandler object.
    """
    assert isinstance(logger_att.stream_handler(), logging.StreamHandler)


def test_get_logger(logger: logging.Logger) -> None:
    """Tests if logger returns logging.Logger object.
    """
    assert isinstance(logger, logging.Logger)


def test_close_logger(logger: logging.Logger) -> None:
    """Tests if close_logger closes all handlers.
    """
    close_logger(logger)
    assert logger.handlers == []
