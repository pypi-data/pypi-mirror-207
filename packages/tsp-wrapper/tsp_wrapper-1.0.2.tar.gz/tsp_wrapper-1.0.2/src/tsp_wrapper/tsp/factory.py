from typing import Callable

from .types import TSPMiddleware

tsp_solver_funcs: dict[str, Callable[..., TSPMiddleware]] = {}


def register(converter_name: str, converter_fn) -> None:
    """Register a new converter middleware."""
    tsp_solver_funcs[converter_name] = converter_fn


def unregister(converter_name: str) -> None:
    """Unregister a converter middleware."""
    tsp_solver_funcs.pop(converter_name, None)


def create(converter_name: str):
    try:
        converter_func = tsp_solver_funcs[converter_name]
    except KeyError:
        raise ValueError(f"unknown converter {converter_name !r}") from None
    return converter_func()
