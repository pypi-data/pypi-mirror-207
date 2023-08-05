# flake8: noqa
from tsp_wrapper.conf.global_settings import *

try:
    from tsp_wrapper.conf.settings import *
except ModuleNotFoundError:
    pass

__all__ = [
    "MIDDLEWAR",
    "TSP_CONVERTER",
    "BROKER_URL",
    "INBOUND_QUEUE",
    "OUTBOUND_QUEUE",
]
