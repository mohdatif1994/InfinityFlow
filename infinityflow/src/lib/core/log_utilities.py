import os
import logging
from datetime import datetime

class LoggerConfig:
    def __init__(self, name='my_logger', log_file='app.log', log_level=logging.DEBUG):
        self.name = name
        self.log_file = log_file
        self.log_level = log_level
        self.logger = self._setup_logger()

    def _setup_logger(self):
        # Create a logger object
        logger = logging.getLogger(self.name)
        logger.setLevel(self.log_level)

        # Create a file handler
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO if self.log_level==logging.DEBUG else logging.CRITICAL)  # Console handler logs WARNING and above

        # Create a formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        if not logger.hasHandlers():
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger

    def get_logger(self):
        if self.logger is None:
            self.logger = self._setup_logger()
        return self.logger
    
    @staticmethod
    def get_logging_file(class_name, log_file_path):

        folder_name = f"{class_name}{datetime.now().strftime('%Y%m%d_%H%M%S')}".upper()
        if not os.path.exists(log_file_path):
            os.mkdir(log_file_path)
        
        if not os.path.exists(os.path.join(log_file_path, folder_name)):
            os.mkdir(os.path.join(log_file_path, folder_name))
        
        path = os.path.join(log_file_path, folder_name, 'infinity_flow.log')
        return path 
    
# Usage example
if __name__ == "__main__":
    log_config = LoggerConfig(name='my_custom_logger', log_file='custom.log', log_level=logging.INFO)
    logger = log_config.get_logger()

    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')