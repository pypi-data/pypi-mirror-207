from kombu import Connection
import time
from tsp_wrapper.conf import BROKER_URL

#: The global broker instance.
global_broker = None


def get_broker() -> Connection:
    """Get the global broker instance.

    If no global broker is set, a Kombu RabbitMQ broker will be returned.

    Returns:
      KombuConnection: The default rabbitmq connection.
    """
    global global_broker
    if global_broker is None:
        set_broker(Connection(BROKER_URL))

    return global_broker


def set_broker(broker: Connection):
    """Configure the global broker instance.

    Parameters:
      broker(Connection): The kombu Connection instance to use by default.
    """
    global global_broker
    global_broker = broker


def connect_broker():
    try:
        broker = get_broker()
        broker.connect()
    except (ConnectionRefusedError, ConnectionResetError) as ex:
        print(f"cannot connect to {broker} with error {ex}")
        time.sleep(1)
        connect_broker()
        # raise ConnectionError(f"cannot connect to {broker}")
