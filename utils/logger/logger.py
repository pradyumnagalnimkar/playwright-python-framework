import os
from utils.logger.base_logger import BaseLogger
import logging


class Logger(BaseLogger):
    def __init__(self):
        self._logger = None

        """Setup logging module"""
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)

        """Create file handler and set its level to DEBUG"""
        file_name = "execution_logs.log"
        filepath = os.path.join(os.getcwd(),'logs')
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        file_handler = logging.FileHandler(f"{filepath}/{file_name}", 'a')
        file_handler.setLevel(logging.DEBUG)

        """Create console handler and set its level to INFO"""
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        """Create Formatter and set formatter to above handlers"""
        formatter = logging.Formatter("%(asctime)s - [%(filename)s - %(lineno)s] - [%(levelname)s] - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        """Add handlers to the logger"""
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def debug(self, message):
        self._logger.debug(message, stacklevel=2)

    def info(self, message):
        self._logger.info(message, stacklevel=2)

    def warning(self, message):
        self._logger.warning(message, stacklevel=2)

    def error(self, message):
        self._logger.error(message, stacklevel=2)

    def critical(self, message):
        self._logger.critical(message, stacklevel=2)