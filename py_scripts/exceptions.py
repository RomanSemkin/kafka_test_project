class PostgresCredentialsError(Exception):
    msg = "Invalid credentials"


class PostgreConnectionException(Exception):
    msg = "Connection fails"


class PostgresDataError(Exception):
    msg = "SQl query is not valid"
