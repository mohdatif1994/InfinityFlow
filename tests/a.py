import logging
import argparse


class LoggerExample:
    @classmethod
    def setup_logging(cls, log_level):
        # Convert log_level string to corresponding logging level
        print(log_level.upper())
        log_level = getattr(logging, log_level.upper(), logging.INFO)
        d_log_level = getattr(logging, 'DEBUG', logging.INFO)
        
        # Set up the root logger
        logger = logging.getLogger()
        logger.setLevel(log_level)
        
        # Create a file handler
        file_handler = logging.FileHandler("example.log")
        file_handler.setLevel(d_log_level)
        
        # Create a console handler
        console_handler = logging.StreamHandler()
        print("******", log_level, logging.DEBUG, logging.INFO)
        console_handler.setLevel(log_level if log_level > logging.DEBUG else logging.INFO)
        
        # Create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        # Store the logger in the class
        cls.logger = logger

    @classmethod
    def get_args(cls):
        parser = argparse.ArgumentParser(description="Process some arguments.")
        parser.add_argument('--log_level', type=str, default='INFO', help='Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)')
        args = parser.parse_args()
        return args

    @classmethod
    def process_args(cls):
        args = cls.get_args()
        cls.setup_logging(args.log_level)
        
        cls.logger.debug("This is a debug message")
        cls.logger.info("This is an info message")
        cls.logger.warning("This is a warning message")
        cls.logger.error("This is an error message")
        cls.logger.critical("This is a critical message")

def main():
    LoggerExample.process_args()

if __name__ == "__main__":
    main()