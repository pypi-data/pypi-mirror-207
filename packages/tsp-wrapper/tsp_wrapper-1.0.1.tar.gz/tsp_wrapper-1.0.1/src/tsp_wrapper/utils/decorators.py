"""Functions that help with dynamically creating decorators for tasks."""

from tsp_wrapper.tasks import Task
from functools import wraps


def task(validators: list = []):  # noqa
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            return func(*args, **kwargs)

        setattr(func, "publish", Task(func=func, validators=validators).run)  # noqa
        return func

    return decorator
