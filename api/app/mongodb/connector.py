"""connector helps us connect mongodb"""
from contextlib import contextmanager

from mongoengine import connect
from decouple import config


def make_connection():
    return connect(host=config("DATABASE_URL"))


@contextmanager
def handle_connection():
    connection = make_connection()
    yield connection
    connection.close()
