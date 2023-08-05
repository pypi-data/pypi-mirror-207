import configparser
import json
from typing import Dict, Protocol

import toml
import yaml


class Loader(Protocol):
    def load(self, f) -> Dict:
        pass


class ConfigLoader:
    """A factory class for loading configuration files"""

    @staticmethod
    def load_config_file(filename: str) -> Dict:
        """Load a configuration file"""
        file_type = filename.split(".")[-1]
        with open(filename, "r") as f:
            loader = ConfigLoader._get_loader(file_type)
            return loader.load(f)

    @staticmethod
    def _get_loader(file_type: str):
        """Factory method to get a loader object"""
        loaders = {
            "yaml": YAMLLoader(),
            "ini": INILoader(),
            "json": JSONLoader(),
            "toml": TOMLLoader(),
        }
        try:
            return loaders[file_type]
        except KeyError:
            raise KeyError(f"Invalid file type: {file_type}")


class YAMLLoader:
    """A loader class for YAML configuration files"""

    def load(self, f: str) -> Dict:
        return yaml.safe_load(f)


class INILoader:
    """A loader class for INI configuration files"""

    def load(self, f: str) -> Dict:
        config = configparser.ConfigParser()
        config.read_file(f)
        return {section: dict(config[section]) for section in config.sections()}


class JSONLoader:
    """A loader class for JSON configuration files"""

    def load(self, f: str) -> Dict:
        return json.load(f)


class TOMLLoader:
    """A loader class for TOML configuration files"""

    def load(self, f: str) -> Dict:
        return toml.load(f)
