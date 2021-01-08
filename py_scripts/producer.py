from pykafka import KafkaClient
from pykafka import exceptions

import settings
from site_checker import SiteChecker


URL = settings.URL

site = SiteChecker(URL)

try:
    client = KafkaClient(hosts=f"{settings.KAFKA_HOST}:{settings.KAFKA_PORT}")
except exceptions.NoBrokersAvailableError:
    print("Kafka host is not available")
    client = None

if client:
    topic = client.topics["web-site"]
    print("Topic is ", topic)
    if topic:
        with topic.get_producer() as producer:
            site_data = bytes(site.check().encode("utf-8"))
            producer.produce(site_data)
            print("Message was produced.")
