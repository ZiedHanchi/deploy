import sys
import os
from os.path import dirname, realpath, sep, pardir
from pathlib import Path

if dirname(realpath(__file__)) not in sys.path :
    sys.path.append(dirname(realpath(__file__)))
if dirname(os.getcwd()) not in sys.path :
    sys.path.append(os.getcwd())
if Path(os.path.dirname(os.path.realpath(__file__))).parent not in sys.path :
    sys.path.append(str(Path(os.path.dirname(os.path.realpath(__file__))).parent))  
if Path(os.path.dirname(os.path.realpath(__file__))).parent.parent not in sys.path :
    sys.path.append(str(Path(os.path.dirname(os.path.realpath(__file__))).parent.parent))  


import logging
from logging.handlers import TimedRotatingFileHandler
import pathlib

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s —"
    "%(funcName)s:%(lineno)d — %(message)s")
LOG_DIR = PACKAGE_ROOT / 'logs'
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / 'ml_api.log'


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(
        LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(logging.WARNING)
    return file_handler


def get_logger(*, logger_name):
    """Get logger with prepared handlers."""

    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.INFO)

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False

    return logger


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = ''
    SERVER_PORT = 5000


class ProductionConfig(Config):
    DEBUG = False
    SERVER_PORT = os.environ.get('PORT', 5000)


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
