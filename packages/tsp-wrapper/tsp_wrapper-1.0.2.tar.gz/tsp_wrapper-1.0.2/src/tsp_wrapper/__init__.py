from tsp_wrapper.broker import set_broker, get_broker, connect_broker

from tsp_wrapper.tsp.loader import load_plugins
from tsp_wrapper.conf import MIDDLEWARE


__all__ = [
    # Brokers
    "get_broker",
    "set_broker",
]

__version__ = "1.0.2"


def setup():
    load_plugins(MIDDLEWARE)
    connect_broker()
