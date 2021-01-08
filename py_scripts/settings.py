import os

POSTGRES_HOST = os.environ.get("POSTGRES_MAIN_HOST", "localhost")
POSTGRES_PORT = os.environ.get("POSTGRES_MAIN_PORT", "5432")
POSTGRES_NAME_DB = os.environ.get("POSTGRES_MAIN_NAME", "main_db")
POSTGRES_USERNAME = os.environ.get("POSTGRES_MAIN_USERNAME", "admin")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_MAIN_PASSWORD", "admin")

KAFKA_FETCH_SIZE = 5
KAFKA_HOST = os.environ.get("KAFKA_HOST", "localhost")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")


URL = "https://yandex.ru"
