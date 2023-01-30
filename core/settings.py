from environs import Env

env = Env()
env.read_env()

Env = env.str('FAST_ENV', default='production')
DEBUG = ENV = 'development'
SQLALCHEMY_DATABASE_URL = env.str('SQLALCHEMY_DATABASE_URL')