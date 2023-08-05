from dataclasses import dataclass

from tsp_wrapper.tsp import factory
import math


@dataclass
class EuclideanMiddleware:
    def convert(self, data: dict) -> dict:
        """Creates callback to return distance between points."""
        distances: dict = {}
        cities = data["cities"]
        for src in cities:
            distances[src.name] = {}
            for dest in cities:
                if src.name == dest.name:
                    distances[src.name][dest.name] = 0
                else:
                    # Euclidean distance
                    distances[src.name][dest.name] = int(
                        math.hypot((src.location.lat - dest.location.lat), (src.location.lng - dest.location.lng))
                    )
        data["distances"] = distances
        return data


def register() -> None:
    factory.register("euclidean", EuclideanMiddleware)
