from kombu.mixins import ConsumerMixin
from enum import Enum

from .queues import get_queues


class WorkerType(Enum):
    inbound = "inbound"
    outbound = "outbound"


class Worker(ConsumerMixin):
    def __init__(self, connection, handler, type: str = WorkerType.inbound.value):
        self.connection = connection
        self._type = type
        self.handler = handler

    def get_consumers(self, Consumer, channel):
        queues = get_queues()
        return [
            Consumer(
                queues=queues.outbound if self._type == WorkerType.outbound.value else queues.inbound,
                accept=["pickle", "json"],
                callbacks=[self.process_task],
            )
        ]

    def process_task(self, body, message):
        print(f"Got task {body}")
        try:
            if self._type == "inbound":
                self.handler.publish(args=(body["message"],))
            else:
                self.handler(body["message"])
            # only in case of successful task process we can remove the task from the queue
            message.ack()
        except Exception as exc:
            print("task raised exception: %r", exc)
