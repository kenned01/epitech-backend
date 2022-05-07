import psycopg2
from psycopg2 import pool
import os


class DataBase(object):
    class __DataBase:
        def __init__(self):
            self.connectionPool = getConnectionPool()

        def __str__(self):
            return self

        def close(self):
            if self.connectionPool:
                self.connectionPool.closeall()

    instance = None

    def __new__(cls):
        if not DataBase.instance:
            DataBase.instance = DataBase.__DataBase()

        return DataBase.instance


def getConnectionPool():
    connectionPool = None

    try:
        connectionPool = pool.SimpleConnectionPool(
            1,
            20,
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PWD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )

    except (Exception, psycopg2.Error) as error:
        print('Error while connecting to DB' + error.__str__())

    return connectionPool
