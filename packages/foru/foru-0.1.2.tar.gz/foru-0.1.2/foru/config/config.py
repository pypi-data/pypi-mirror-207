import os
from foru.config import global_settings
import configparser
import logging


logger = logging.getLogger('foru.config')


def init_config():
    home = os.path.expanduser('~')
    config_dir = os.path.join(home, global_settings.config_dir)
    if not os.path.exists(config_dir):
        os.mkdir(config_dir)
    cp = configparser.ConfigParser()
    config_file = os.path.join(config_dir, global_settings.config_file)
    if not os.path.exists(config_file):
        logger.debug(f'{config_file} does not exists.')
        cp['foru'] = {
            'server': 'localhost',
            'port': '9527'
        }
        with open(config_file, 'w') as f:
            cp.write(f)
    else:
        with open(config_file) as f:
            cp.read_file(f)
    logger.debug(f'configuration: {cp.__dict__["_sections"]}')
    return cp
