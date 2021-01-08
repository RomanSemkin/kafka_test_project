from psycopg2._psycopg import (
    OperationalError,
    ProgrammingError,
    IntegrityError,
    DataError,
)
from psycopg2 import connect

import exceptions


class PostgresConnection:
    def __init__(self, connection_info):
        self.connection_info = connection_info
        self._connection = None
        self.cursor = None

    def connect(self):
        try:
            self._connection = connect(**self.connection_info)
        except OperationalError as e:
            if e.args and "password authentication failed" in e.args[0]:
                raise exceptions.PostgresCredentialsError from e
            if e.args and "timeout expired" in e.args[0]:
                raise exceptions.PostgreConnectionException from e
            raise exceptions.PostgreConnectionException from e
        self.cursor = self._connection.cursor()
        self._connection.autocommit = True
        return self

    def close(self):
        return self._connection.close()

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def call(self, query, params=None):
        try:
            self.cursor.execute(query, params)
        except (ProgrammingError, IntegrityError) as e:
            raise exceptions.PostgreConnectionException from e
        except DataError as e:
            raise exceptions.PostgresDataError from e

        if self.cursor.description:
            return self.cursor.fetchone()

    def copy(self, file, table_name, columns):
        try:
            self.cursor.copy_from(file, table_name, columns)
        except (ProgrammingError, IntegrityError) as e:
            raise exceptions.PostgreConnectionException from e
        except DataError as e:
            raise exceptions.PostgresDataError from e
