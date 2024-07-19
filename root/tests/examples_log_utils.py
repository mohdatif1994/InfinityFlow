"""This File contains exmaples of the log utils Librries."""
import unittest
import logging
from root.project.lib.log_utils import LoggerConfig

class TestLogUtils(unittest.TestCase):

    def test_log_utils_with_info_arguments(self):
        log_config = LoggerConfig(name='my_custom_logger', log_file=f"/Users/mohdatifkhan/Desktop/testing_branch/automation_coding/root/tests/{TestLogUtils.__name__}{'.log'}", log_level=logging.INFO)
        log = log_config.get_logger()
        #log = LoggerUtils(f"/Users/mohdatifkhan/Desktop/testing_branch/automation_coding/root/tests/{TestLogUtils.__name__}{'.log'}")
        log.info("Inside test_log_utils_with_info_arguments")
        log.error("Error.....Error")
        log.debug("Debug.....Debug")
        log.critical("Critical....Critical")
        log.warning("Warning.....Warning")
        log.info("-----End-----")
    
    def test_log_utils_with_debug_arguments(self):
        log_config = LoggerConfig(name='my_custom_logger', log_file=f"/Users/mohdatifkhan/Desktop/testing_branch/automation_coding/root/tests/{TestLogUtils.__name__}{'.log'}", log_level=logging.DEBUG)
        log = log_config.get_logger()
        log.info("Inside test_log_utils_with_debug_arguments")
        log.error("Error.....Error")
        log.debug("Debug.....Debug")
        log.critical("Critical....Critical")
        log.warning("Warning.....Warning")
        log.info("-----End-----")

if __name__ == '__main__':
    unittest.main()