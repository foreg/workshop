import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/workshop'
    SQLALCHEMY_TRACK_MODIFICATIONS = False