import os
import logging
import argparse
from infinityflow.src.lib.core.config import Config
from infinityflow.src.lib.core.host_info import HostInfo
from infinityflow.src.lib.core.constant import HostAttributes
from infinityflow.src.lib.core.log_utilities import LoggerConfig

class BaseTest:
    def __init__(self, config, logging, args):
        self._config = config
        self._log = logging
        self._args = args

    def setup(self):
        self._log.error("djfsajd")
        return True

    def execute(self):
        return True

    def cleanup(self):
        return True

    @staticmethod
    def get_default_config_path():
        host_folder_path = HostAttributes.HostPath.value[HostInfo.get_host_info()['os_name'].lower()] 
        config_path = os.path.join(host_folder_path, 'config.yaml')
        return config_path
    
    @classmethod
    def get_args(cls):
        parser = argparse.ArgumentParser(description="Process some arguments.")
        parser.add_argument('--config', default=BaseTest.get_default_config_path(), type=str, help='Config File Path')
        parser.add_argument('--console_log', default=logging.DEBUG, type=str, help='')
        parser.add_argument('--log_path', default=None, type=str, help='')

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
        logging_file = LoggerConfig.get_logging_file(class_name=class_name.__name__, log_file_path=log_file_path)
        
        #  Create Logging objects
        logging_obj = LoggerConfig(name='my_logger', log_file=logging_file, log_level=args.console_log)
        logger = logging_obj.get_logger()

        logger.info("----------")
        #  Create Object of the Test Cases which need to execute.    
        try:
            obj = cls(cfgs, logger, args)
        except Exception as ex:
            logger.error(f"Test Failed -{ex}")
            logger.error(f"******Test Failed*****")
            return False

        #  Execute the SetUp of Test Cases 
        try:
            return_flag = obj.setup()
        except Exception as ex:
            logger.error(f"Test Failed-{ex}")
            return_flag = False
        finally:
            if not return_flag:
                logger.error(f"******Test Failed*****")
                return False
            
        #  Execute the Execute of Test Cases 
        try:
            return_flag = obj.execute()
        except Exception as ex:
            logger.error(f"Test Failed-{ex}")
            return_flag = False
        finally:
            if not return_flag:
                logger.error(f"******Test Failed*****")
                return False

        #  Execute the Cleanup of Test Case
        try:
            return_flag = obj.cleanup()
        except Exception as ex:
            logger.error(f"Test Failed-{ex}")
            logger.error(f"******Test Failed*****")
            return_flag = False
        finally:
            if not return_flag:
                return False
            logger.info("******Test Passed*****")

        return return_flag
    