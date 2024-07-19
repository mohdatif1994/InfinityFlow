"""Base Code for each Test"""
import argparse

class CommonTest(object):

    def __init__(self, cfg):
        self._log = None
    
    def execute(self):
        """
        Test Step Execution.
        
        Returns:
            bool: True if Pass
        """
        pass

    @classmethod
    def get_args(cls):
        parser = argparse.ArgumentParser(description="Process some arguments.")
        parser.add_argument('--config', default="C:\InfinityFlow\config.yaml", type=str, help='Config File Path')
        args = parser.parse_args()
        return args
    
    @classmethod
    def process_args(cls):
        args = cls.get_args()
        # Process the arguments as needed
        if args.config:
            print(f"Config Argument received: {args.config}")
    

    @classmethod
    def main():
        
        args = cls.get_args()
