"""Represents a basic tsp middleware."""

from typing import Protocol


class TSPMiddleware(Protocol):
    """Basic representation of a tsp middleware."""

    def convert(self) -> None:
        """Let the message convert to diffrent format."""
