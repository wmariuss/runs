import os
from glob import iglob
import yaml
import logging


class Config(object):
    def __init__(self, path=None):
        self.current_dir = os.path.dirname(__file__)
        self.path = path or os.environ.get('CONFIGS_PATH', '~/runs')
        self.files_list = iglob(f'{self.path}/*.yml')

    def files(self):
        return [files for files in self.files_list]

    def parse(self):
        config_list = {}
        for f in self.files():
            with open(f, 'r') as conf:
                try:
                    config = yaml.load(conf, Loader=yaml.FullLoader)
                    config_list.update(config)
                except yaml.YAMLError:
                    logging.fatal('Config file parse error: {f}',
                                  exc_info=True)
        return config_list

    def get(self, service):
        config_list = self.parse()
        param_list = {}

        if service == 'alerta':
            if service in config_list:
                param_list = config_list.get(service)

        return param_list
