from kombu import Exchange, Queue
from dataclasses import dataclass
from tsp_wrapper.conf import EXCHANGE_NAME, INBOUND_QUEUE, OUTBOUND_QUEUE


#: The global Queue and Exchange instances.
global_exchange = Exchange(EXCHANGE_NAME, type="direct")
global_queues = None


@dataclass
class Queues:
    inbound: list[Queue]
    outbound: list[Queue]


def set_queues(queues: Queues):
    """Configure the global Queues instance.

    Parameters:
      queues(Queues): The Queues instance to use by default.
    """
    global global_queues
    global_queues = queues


def set_exchange(exchange: Exchange):
    global global_exchange
    global_exchange = exchange


def get_queues() -> Queues:
    """Get the global Queuese instance.

    If no global queues is set, a Queues object with inbound and outbound name queues will be returned.

    Returns:
      Queues: The default Queues instance.
    """
    global global_queues
    global global_exchange
    if global_queues is None:
        set_queues(
            queues=Queues(
                inbound=[Queue(INBOUND_QUEUE, global_exchange, routing_key=INBOUND_QUEUE)],
                outbound=[Queue(OUTBOUND_QUEUE, global_exchange, routing_key=OUTBOUND_QUEUE)],
            )
        )
    return global_queues  # type: ignore


def get_exchange() -> Exchange:
    global global_exchange
    return global_exchange
