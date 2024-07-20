
class TestFail(Exception):
    """
    Exception raised for TestFail in the configuration.
    """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class ConfigError(Exception):
    """
    Exception raised for errors in the configuration.
    """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
