from configparser import ConfigParser

class ConfigProvider:
    @staticmethod
    def read_config(conf_name):
        file_path = f'../{conf_name}.ini'
        config = ConfigParser()
        config.read(file_path)
        return config