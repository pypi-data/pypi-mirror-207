from tsp_wrapper.broker import get_broker, send_data
from tsp_wrapper.conf import OUTBOUND_QUEUE
from typing import Callable


class Task:
    def __init__(self, func: Callable, validators: list[Callable]) -> None:
        self.func = func
        self.validators = validators

    def run(self, args: tuple = (), kwargs: dict = {}) -> None:  # noqa
        """
        Example:
        >>> @task()
            def bar(s,b):
            print(f'Message: {s} {b}')
        >>> bar.publish(args = ("hi", "ds") )
        >>> Message: hi ds
        """
        for validator in self.validators:
            validator(*args, **kwargs)
        results = self.func(*args, **kwargs)
        send_data(connection=get_broker(), message=results, routing_key=OUTBOUND_QUEUE)
