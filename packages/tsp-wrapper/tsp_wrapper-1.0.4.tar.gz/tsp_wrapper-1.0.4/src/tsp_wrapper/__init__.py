from tsp_wrapper.broker import set_broker, get_broker, connect_broker

from tsp_wrapper.tsp.loader import load_plugins
from tsp_wrapper.conf import MIDDLEWARE, INBOUND_QUEUE, OUTBOUND_QUEUE


__all__ = [
    # Brokers
    "get_broker",
    "set_broker",
    # Variables
    "INBOUND_QUEUE",
    "OUTBOUND_QUEUE",
]

__version__ = "1.0.4"


def setup():
    load_plugins(MIDDLEWARE)
    connect_broker()
