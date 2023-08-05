from .queues import get_exchange
from kombu.pools import producers


def send_data(connection, message, routing_key):
    payload = {"message": message}
    exchange = get_exchange()
    with producers[connection].acquire(block=True) as producer:
        producer.publish(
            payload,
            serializer="pickle",
            compression="bzip2",
            exchange=exchange,
            declare=[exchange],
            routing_key=routing_key,
        )
