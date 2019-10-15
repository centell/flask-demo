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

MYSQL_DATABASE = config('MYSQL_DATABASE')
MYSQL_USER = config('MYSQL_USER')
MYSQL_ROOT_PASSWORD = config('MYSQL_ROOT_PASSWORD')
MYSQL_PASSWORD = config('MYSQL_PASSWORD')
MYSQL_PORT = config('MYSQL_PORT')
MYSQL_HOSTNAME = config('MYSQL_HOSTNAME')

# SQL ALCHEMY Configuration

# System Variable Configuration

# Error Messages
SIGN_IN_ERRORS = dict(
    SUCCESS='성공',
    WRONG_PASSWORD='비밀번호가 일치하지 않습니다.',
    WRONG_OTP='OTP 인증번호를 확인해주십시오.',
    BLOCKED_SIGN_IN='접근이 차단되었습니다.',
    INACTIVATED='존재하지 않는 회원입니다.'
)
