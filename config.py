import os
from os.path import join, dirname
from dotenv import load_dotenv


def get_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    return os.getenv(key)


def config(key):
    if get_env('ENV') == 'development':
        return get_env(key)
    elif get_env('ENV') == 'test':
        return get_env('TEST' + key)
    elif get_env('ENV') == 'production':
        return get_env('PRO' + key)


# Server Configuration
ENV = get_env('ENV')
DEBUG = config('DEBUG')
TESTING = config('TESTING')

HOST = config('HOST')
PORT = config('PORT')

# Database Configuration
MYSQL_DATABASE = config('MYSQL_DATABASE')
MYSQL_USER = config('MYSQL_USER')
MYSQL_ROOT_PASSWORD = config('MYSQL_ROOT_PASSWORD')
MYSQL_PASSWORD = config('MYSQL_PASSWORD')
MYSQL_PORT = config('MYSQL_PORT')
MYSQL_HOSTNAME = config('MYSQL_HOSTNAME')
