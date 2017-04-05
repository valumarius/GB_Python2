import sqlite3
from contextlib import closing
from time import time
from datetime import datetime


def timeit(method):
    def timed(*args, **kw):
        ts = time()
        result = method(*args, **kw)
        te = time()
        print('[TimeIt] func: "{}" run in {} ms'.format(method.__name__, (te - ts) * 1000))
        return result
    return timed


def db_conn():
    conn = sqlite3.connect('db.db')
    return conn


# Функция работы с БД (подключение, создание)
@timeit
def db_create():
    print("Создаем/пересоздаем БД")
    with open('create_tables.sql') as sqlfile:
        query = sqlfile.read()
    with closing(db_conn().cursor()) as curr:
        curr.executescript(query)
        return None
