import io
import json

class Config:
    def __init__(self, config_file):
        self._config_file = config_file
        self.load_config()

    def load_config(self):
        """
        Args:
            _config_file: file name.
        Returns:
            config object.
        """
        config = None
        with io.open(self._config_file, 'r', encoding='utf-8') as f:
            self._config = json.load(f)
        
    def save_config(self):
        """
        Save the config into a json file.
        """
        with open(self._config_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self._config, ensure_ascii=False, indent=3))
            logging.debug(f"Wrote file '{self._config_file}'.")    
    
    def __getitem__(self, key):
        return self._config[key]

    def __setitem__(self, key, value):
        self._config[key] = value