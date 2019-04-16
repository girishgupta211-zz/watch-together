"""
environment configuration
"""

import os

from dotenv import load_dotenv

WATCH_TOGETHER_ENV_PATH = os.getenv('WATCH_TOGETHER_ENV_PATH', '.')

if WATCH_TOGETHER_ENV_PATH:
    load_dotenv(dotenv_path=WATCH_TOGETHER_ENV_PATH + '/.env')
else:
    raise Exception(
        'Environment variables file path is missing. Loading defaults')


class Config(object):
    """
    Base config class
    """
    DEBUG = False
    ENV = os.getenv('FLASK_CONFIG', 'dev')
    TIME_ZONE = os.getenv('TIME_ZONE', 'Asia/Kolkata')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    POSTGRES_URI = 'postgresql://{user}:{password}@{host}:{port}/{db}'.format(
        user=POSTGRES_USER, password=POSTGRES_PASSWORD, host=POSTGRES_HOST,
        port=POSTGRES_PORT, db=POSTGRES_DB
    )
    CMS_TOKEN = os.getenv('CMS_TOKEN')
    LOGGING_DIR = os.getenv('LOGGING_DIR', '/tmp/')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
