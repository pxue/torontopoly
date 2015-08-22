import os

HOST = "0.0.0.0"
PORT = 8080

class Config(object):
    SECRET_KEY = os.urandom(56)

class DevelopmentConfig(Config):
    DEBUG = True
