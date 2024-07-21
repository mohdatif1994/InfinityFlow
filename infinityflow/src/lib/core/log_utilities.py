"""Logging Utilities"""
from __future__ import annotations

import logging
import os
from datetime import datetime


class LoggerConfig:
    """Logger Config Class"""

    def __init__(self, name, log_file, log_level):
        self.name = name
        self.log_file = log_file
        self.log_level = log_level
        self.logger = self._setup_logger()

    def _setup_logger(self):
        """Method to Setup Logger"""
        # Create a logger object
        log = logging.getLogger(self.name)
        log.setLevel(self.log_level)

        # Create a file handler
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler
        console_handler = logging.StreamHandler()
        check = self.log_level == logging.DEBUG
        console_handler.setLevel(
            logging.INFO if check else logging.CRITICAL,
        )  # Console handler logs WARNING and above

        # Create a formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] "
            "%(message)s - %(funcName)s ",
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        if not log.hasHandlers():
            log.addHandler(file_handler)
            log.addHandler(console_handler)

        return log

    def get_logger(self):
        """Get Logger object"""
        if self.logger is None:
            self.logger = self._setup_logger()
        return self.logger

    @staticmethod
    def get_logging_file(class_name, log_file_path):
        """Method to fine the Logging File"""
        date_now = datetime.now().strftime("%Y%m%d_%H%M%S")
        folder_name = f"{class_name}{date_now}".upper()
        if not os.path.exists(log_file_path):
            os.mkdir(log_file_path)

        if not os.path.exists(os.path.join(log_file_path, folder_name)):
            os.mkdir(os.path.join(log_file_path, folder_name))

        path = os.path.join(log_file_path, folder_name, "infinity_flow.log")
        return path


# Usage example
if __name__ == "__main__":
    log_config = LoggerConfig(
        name="my_custom_logger",
        log_file="custom.log",
        log_level=logging.INFO,
    )
    logger = log_config.get_logger()

    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
