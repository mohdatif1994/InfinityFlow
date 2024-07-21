"""This Class is created for Base Template for all Test Cases."""
from __future__ import annotations

import argparse
import logging
import os

from infinityflow.src.lib.core.config import Config
from infinityflow.src.lib.core.constant import HostAttributes
from infinityflow.src.lib.core.host_info import HostInfo
from infinityflow.src.lib.core.log_utilities import LoggerConfig


class BaseTest:
    """Base Test for All Test Cases."""

    def __init__(self, config, log, args):
        self._config = config
        self._log = log
        self._args = args

    def setup(self):
        """Setup.

        Returns:
            bool: True/False
        """
        return True

    def execute(self):
        """Execute.

        Returns:
            bool: True/False
        """
        return True

    def cleanup(self):
        """Cleanup.

        Returns:
            bool: True/False
        """
        return True

    @staticmethod
    def get_default_config_path():
        """
        This method is to get the default config Path.

        Returns:
            path: config path.
        """
        host_folder_path = HostAttributes.HOST_PATH.value[
            HostInfo.get_host_info()["os_name"].lower()
        ]
        config_path = os.path.join(host_folder_path, "config.yaml")
        return config_path

    @classmethod
    def get_args(cls):
        """This method is to get Args at runtime.

        Returns:
            args: str
        """
        parser = argparse.ArgumentParser(description="Process some arguments.")
        parser.add_argument(
            "--config",
            default=BaseTest.get_default_config_path(),
            type=str,
            help="Config File Path",
        )
        parser.add_argument(
            "--console_log",
            default=logging.DEBUG,
            type=str,
            help="",
        )
        parser.add_argument("--log_path", default=None, type=str, help="")

        args = parser.parse_args()
        return args

    @classmethod
    def main(cls, class_name):
        """
        This is main class which does details: -
        - Create Config objects
        - Get the cfgs objects.
        - Create Logging objects.
        - Create Object of the Test Cases which need to execute.
        - Execute the SetUp of Test Cases.
        - Execute the execute of the Test Cases.
        - Execute the cleanup of the Test Cases.

        Args:
            class_name: class name of the TestCase.

        Returns:
            bool: True if Test Pass else Fail.
        """
        #  Flag to decide the Test Failed or Passed
        return_flag = True

        #  Get the Argument passed at runtime from the Console
        args = cls.get_args()

        #  Create Config objects
        config = Config(config_path=args.config)

        #  Get the cfgs objects.
        cfgs = config.get_cfg_opts()
        if args.log_path is None:
            log_file_path = Config.get_logging_path(cfg=cfgs)
        else:
            log_file_path = args.log_path

        #  Get the Log File Path
        logging_file = LoggerConfig.get_logging_file(
            class_name=class_name.__name__,
            log_file_path=log_file_path,
        )

        #  Create Logging objects
        logging_obj = LoggerConfig(
            name="my_logger",
            log_file=logging_file,
            log_level=args.console_log,
        )
        logger = logging_obj.get_logger()

        #  Create Object of the Test Cases which need to execute.
        try:
            obj = cls(cfgs, logger, args)
        except OSError as ex:
            logger.error("Test Failed - %s", ex)
            logger.error("******Test Failed*****")
            return False

        #  Execute the SetUp of Test Cases
        try:
            return_flag = obj.setup()
        except OSError as ex:
            logger.exception("Test Failed - %s", ex)
            return_flag = False

        if not return_flag:
            logger.error("******Test Failed*****")
            obj.cleanup()
            return False

        #  Execute the Execute of Test Cases
        try:
            return_flag = obj.execute()
        except OSError as ex:
            logger.exception("Test Failed - %s", ex)
            return_flag = False

        if not return_flag:
            logger.error("******Test Failed*****")
            obj.cleanup()
            return False

        #  Execute the Cleanup of Test Case
        try:
            return_flag = obj.cleanup()
        except OSError as ex:
            logger.exception("Test Failed - %s", ex)
            return_flag = False

        if not return_flag:
            logger.error("******Test Failed*****")
            return False
        logger.info("******Test Passed*****")

        return return_flag
