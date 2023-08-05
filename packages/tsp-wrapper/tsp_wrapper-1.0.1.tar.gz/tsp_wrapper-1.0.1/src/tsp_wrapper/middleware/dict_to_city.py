from dataclasses import dataclass

from tsp_wrapper.tsp import factory, City, Point


@dataclass
class CityMiddleware:
    def convert(self, data: dict) -> dict:
        cities = list()
        for city in data["locations"]:
            cities.append(City(name=city["name"], location=Point(lat=city["lat"], lng=city["lng"])))
        data["cities"] = cities
        return data


def register() -> None:
    factory.register("city", CityMiddleware)
