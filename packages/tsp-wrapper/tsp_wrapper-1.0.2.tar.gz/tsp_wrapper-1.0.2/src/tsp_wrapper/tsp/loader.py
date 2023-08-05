"""A simple plugin loader."""
import importlib


class ModuleInterface:
    """Represents a middleware interface. A middleware has a single register function."""

    @staticmethod
    def register() -> None:
        """Register the necessary items in the convertor factory."""


def import_module(name: str) -> ModuleInterface:
    """Imports a module given a name."""
    return importlib.import_module(name)  # type: ignore


def load_plugins(plugins: list[str]) -> None:
    """Loads the middlewares defined in the middleware list."""
    for plugin_file in plugins:
        plugin = import_module(plugin_file)
        plugin.register()
