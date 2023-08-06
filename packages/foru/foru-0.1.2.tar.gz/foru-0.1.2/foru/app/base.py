import importlib
import logging.config
import os
import pkgutil
from abc import ABC
from configparser import ConfigParser
from typing import List, Union

import foru.providers
from foru.config.config import init_config
from foru.core import LPlayer
from foru.providers.base import BaseProvider

logger = logging.getLogger('foru.app.base')


class BaseAPP(ABC):
    def __init__(self, player):
        self.init_logger()
        self.cp: ConfigParser = init_config()
        self._player: LPlayer = player
        self._providers: List[BaseProvider] = []
        # default provider index
        self._pi: int = -1
        self._find_providers()

    def add_provider(self, pro):
        self._providers.append(pro)
        # 默认为最后添加的
        self._pi = len(self._providers) - 1

    @property
    def providers(self) -> List[BaseProvider]:
        return self._providers

    def select(self, value):
        if 0 <= value < len(self._providers):
            self._pi = value

    @property
    # @abstractmethod
    def default_provider(self) -> Union[BaseProvider, None]:
        if self._pi != -1:
            return self._providers[self._pi]
        return None

    def _find_providers(self):
        for finder, name, ispkg in pkgutil.iter_modules():
            # logger.debug(f'{finder}, {name}, {ispkg}')
            if name.startswith('foru_'):
                logger.info(f'Find provider: {name}')
                try:
                    pro = importlib.import_module(name)
                    self.add_provider(pro.provider)
                except Exception as e:
                    logger.exception(e)
        # find foru.providers
        for finder, name, ispkg in pkgutil.iter_modules(foru.providers.__path__, foru.providers.__name__ + '.'):
            # logger.debug(f'{finder}, {name}, {ispkg}')
            try:
                if name.split('.')[-1].startswith('foru_'):
                    logger.info(f'Find provider: {name}')
                    pro = importlib.import_module(name)
                    self.add_provider(pro.provider)
            except Exception as e:
                logger.exception(e)

    @property
    def player(self):
        return self._player

    @staticmethod
    def init_logger():
        logger_config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../config/logger.config'))
        print(logger_config_file)
        logging.config.fileConfig(logger_config_file)
