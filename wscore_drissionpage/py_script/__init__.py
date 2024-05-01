import configparser
import os


def read_chrome_options(self):
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', 'credentials.ini')
    config.read(config_path)
    self.browser_path = config['electron']['browser_path']
    self.user_data_dir = config['electron']['user_data_dir']

def read_credentials(self):
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', 'credentials.ini')
    config.read(config_path)
    self.id = config['ShengTen-login']['id']
    self.password = config['ShengTen-login']['password']