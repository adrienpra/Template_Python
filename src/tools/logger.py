"""Modules to generate both .log files and sys.stdout logs.
"""
# logs
import logging
import sys

# type hints
from typing import Self
from dataclasses import dataclass, field

# path
import pathlib
import git

# tools
from tools.utils import git_root, manual_root


@dataclass
class LoggerAttrib:
    """LoggerAttrib is an input class used for creating a logging.Logger.

    Parameters
    ----------
    name : str
        Log file name.
    num_parent : int, optional
        Number of parents between relative position and the root.
        Used in case the project doesn't use git, by default 1.
    setLevel : logging.DEBUG, optional
        Defines level from which logs will be considered by the logger.
        Follows logs' hierarchy, by default logging.DEBUG.
    lvlFile : str, optional
        Defines level from which logs will be displayed.
        Follows logs' hierarchy, by default 'warning'.
    lvlStream : str, optional
        Defines level from which logs will be displayed.
        Follows logs' hierarchy, by default 'debug'.
    """
    name: str
    num_parent: int = 1
    set_level: int = logging.DEBUG
    lvl_file: str = 'warning'
    lvl_stream: str = 'debug'
    mode: str = 'w'
    log_format: str = f'{"%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"}'
    dict_set_level: dict = field(default_factory=lambda: {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    })

    def logs_path(self: Self) -> pathlib.Path:
        """Gets the path to write .log files. By default in root/data/logs/.

        Parameters
        ----------
        self : Self
            Uses LoggerAttrib's name and num_parent.

        Returns
        -------
        pathlib.WindowsPath
            The logs absolute path.
        """
        try:
            root = git_root()
        except git.exc.InvalidGitRepositoryError:
            root = manual_root(self.name, num_parent=self.num_parent)

        p = root / "data/logs"
        return p / f"{self.name}.log"

    def file_handler(self: Self) -> logging.FileHandler:
        """Setup of the file handler (display logs in .log file).
        Calls logs_path() function (previously defined).

        Parameters
        ----------
        self : Self
            Uses LoggerAttrib's name, lvlFile and num_parent.

        Returns
        -------
        logging.FileHandler
            Logger's file handler.
        """
        f_handler = logging.FileHandler(
            LoggerAttrib.logs_path(self), mode=self.mode)
        f_handler.setLevel(self.dict_set_level[self.lvl_file])
        f_handler.setFormatter(logging.Formatter(self.log_format))
        return f_handler

    def stream_handler(self: Self) -> logging.StreamHandler:
        """Setup of the stream handler (display logs in terminal: sys.stdout).

        Parameters
        ----------
        self : Self
            Uses LoggerAttrib's lvlStream.

        Returns
        -------
        logging.StreamHandler
            Logger's stream handler.
        """
        s_handler = logging.StreamHandler(sys.stdout)
        s_handler.setLevel(self.dict_set_level[self.lvl_stream])
        s_handler.setFormatter(logging.Formatter(self.log_format))
        return s_handler


def get_logger(logger_att: LoggerAttrib) -> logging.Logger:
    """Create logger with LoggerAttrib class.

    Parameters
    ----------
    LoggerAttrib : LoggerAttrib
        LoggerAttrib is an input class used for creating a logging.Logger.

    Returns
    -------
    logging.Logger
        Logging library object that manage logs.
    """
    logger = logging.getLogger(logger_att.name)
    logger.setLevel(logger_att.set_level)
    logger.addHandler(logger_att.file_handler())
    logger.addHandler(logger_att.stream_handler())
    return logger


def close_logger(logger: logging.Logger) -> None:
    """Close the logger after use.

    Parameters
    ----------
    logger : logging.Logger
        Logging library object that manage logs.
    """
    logger.handlers.clear()


def main() -> None:
    """Runs if logger.py is run as standalone script.
    """
    # init logger
    logger_att = LoggerAttrib(__name__)
    logger = get_logger(logger_att)

    # log some informations
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")

    # close logger
    close_logger(logger)


if __name__ == "__main__":
    main()
