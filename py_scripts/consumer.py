import json

from pykafka import KafkaClient
from pykafka.common import OffsetType

import settings
from connector import PostgresConnection


def generate_consumer_data(kafka_topic):
    consumer = kafka_topic.get_simple_consumer(
        auto_offset_reset=OffsetType.LATEST,
        reset_offset_on_start=True,
        consumer_timeout_ms=30000,
    )
    # Have no clue what I`m doing :), better to read by chunks here somehow
    yield from (msg for msg in consumer)


def save_site_metrics(data, connection):
    table_name = "site_metrics"
    data_dict = json.loads(data[1].decode("utf-8"))
    query = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s);"

    with connection as c:
        c.call(
            query,
            [
                data[0],
                str(data_dict["code"]),
                str(data_dict["request_time"]),
                str(data_dict["method"]),
                str(data_dict["content-type"]),
            ],
        )
        print("response was sent to the db")


def get_last_pk(connection):
    query = "SELECT kafka_id FROM site_metrics ORDER BY kafka_id DESC LIMIT 1;"

    with connection as c:
        row = c.call(query)
    return row[0] if row else None


if __name__ == "__main__":
    client = KafkaClient(hosts=f"{settings.KAFKA_HOST}:{settings.KAFKA_PORT}")
    topic = client.topics["web-site"]
    print("Topic is ", topic)

    db_connection = PostgresConnection(
        {
            "dbname": settings.POSTGRES_NAME_DB,
            "user": settings.POSTGRES_USERNAME,
            "password": settings.POSTGRES_PASSWORD,
            "host": settings.POSTGRES_HOST,
            "port": settings.POSTGRES_PORT,
        }
    )
    last_pk = get_last_pk(db_connection)
    # instead of this, better to use sql query with batch of messages
    for site_data in generate_consumer_data(topic):
        row = site_data.offset, site_data.value
        if last_pk and site_data.offset <= last_pk:
            print("Message already saved.")
            continue

        save_site_metrics(row, db_connection)
