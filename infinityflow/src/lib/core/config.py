"""This File facilitates the acquisition of configuration parameters from the yaml file."""
import yaml
from pathlib import Path
from infinityflow.src.lib.core.exception import ConfigError

class Config:
    """This class is designed to fetch and process inputs from the yaml configuration Files."""

    def __init__(self, config_path):
        self._config_path = config_path
        self._cfg = None

    def get_cfg_opts(self):
        """
        This method is to get the configuration file opts object.

        Returns:
            cfg: config tags object
        """
        if self._cfg is None:
            try:
                with open(self._config_path, 'r') as file:
                    self._cfg = yaml.safe_load(file.read())
                    if not self._cfg:
                        raise ConfigError("Configuration file is empty.")
            # Further validation of the config can be added here
            except FileNotFoundError:
                raise ConfigError(f"Configuration file not found: {self._config_path}")
            except yaml.YAMLError as exc:
                raise ConfigError(f"Error parsing YAML configuration file: {exc}")
        return self._cfg  
        
    @staticmethod
    def get_logging_cfg(cfg):
        """
        This method extracts the log configuration tags from the YAML file.
        
        Args:
            config_path: 
        """
        try:
            loggign_tags = cfg['core']['logging']
        except KeyError:
            raise ConfigError(f'services tag is missing in config')
        
        return loggign_tags
    
    
