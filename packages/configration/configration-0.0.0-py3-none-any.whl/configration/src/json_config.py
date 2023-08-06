"""Return a valid config object from a json file for the application."""

import json
from termcolor import cprint
import colorama

colorama.init()

ERROR_COLOUR = 'red'

class JsonConfig():
    """
    The class takes a path to a json file and if valid, returns a config dict.

    Attributes
    ----------

    path: str
        The path to the config file

    attrs: dict[str, list[type]
        The dict keys are the fields that are expected in the config json
        The dict item holds a list of allowed types for each files

        If there are attrs, then the config is validated.
    """

    def __init__(self, path: str, attrs: dict[str, list[type]] = {}):
        self.path = path
        self .attrs = attrs
        self.config = self._get_config()
        for key, item in self.config.items():
            self.__dict__[key] = item

    def _get_config(self) -> dict[str, object]:
        # Return config, if contents are valid.
        config = self._read_config()

        if not self.attrs:
            return config

        if self._validate_config(config):
            return config
        quit()

    def _read_config(self) -> dict[str, object]:
        # Open the config file and return the file handle
        try:
            with open(self.path , 'r') as f_config:
                try:
                    return json.load(f_config)
                except json.decoder.JSONDecodeError:
                    cprint(f"Invalid json format in {self.path }", ERROR_COLOUR)
                    quit()
        except FileNotFoundError:
            cprint(f"The file {self.path } is not in the expected location", ERROR_COLOUR)
            quit()

    def _validate_config(self, config: dict[str, type]) -> bool:
        # Return True if structure and values in config are valid.
        for name, item_types in self .attrs.items():
            if name not in config:
                cprint(f"Corrupt config file. {name} missing", ERROR_COLOUR)
                return False
            if type(config[name]) not in item_types:
                cprint(f"Corrupt config file. {name} not of type {item_types}", ERROR_COLOUR)
                return False
        return True
