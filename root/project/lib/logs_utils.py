import logging
class LoggerUtils:

    def __init__(self, file_name, log_level=None):
        arg_log_level = log_level
        log_level = getattr(logging, 'DEBUG', logging.INFO)
        # Set up the root logger
        logger = logging.getLogger()
        logger.setLevel(log_level)
        
        # Create a file handler
        file_handler = logging.FileHandler(file_name)
        file_handler.setLevel(log_level)
        
        # Create a console handler
        console_handler = logging.StreamHandler()
        print("******", log_level, logging.DEBUG, logging.INFO)
        if arg_log_level:
            console_handler.setLevel(log_level)
        else:
            console_handler.setLevel(log_level if log_level > logging.DEBUG else logging.INFO)
        
        # Create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        # Store the logger in the class
        self.logger = logger

if __name__ == "__main__":
    obj = LoggerUtils("abc.log", 'DEBUG')
    obj.logger.debug("Debug")
    obj.logger.info("Info")
    obj.logger.error("Error")
