from tsp_wrapper import broker
from tsp_wrapper.tasks.tsp import tsp_solver_task, get_ans

import typer
import secrets

app = typer.Typer()


@app.command()
def reciver() -> None:
    worker = broker.Worker(connection=broker.get_broker(), handler=get_ans, type="outbound")
    worker.run()


@app.command()
def bridge() -> None:
    worker = broker.Worker(connection=broker.get_broker(), handler=tsp_solver_task, type="inbound")
    worker.run()


@app.command()
def producer() -> None:
    my_data = {
        "locations": [
            {"name": "Nagoya", "lat": 35.1833, "lng": 136.9000},
            {"name": "Taipei", "lat": 25.0375, "lng": 121.5625},
            {"name": "Tongshan", "lat": 34.2610, "lng": 117.1859},
            {"name": "Luanda", "lat": -8.8383, "lng": 13.2344},
        ],
        "num_vehicles": 1,
        "depot": 0,
        "id": secrets.token_hex(5),
    }
    broker.send_data(connection=broker.get_broker(), message=my_data, routing_key="inbound")


@app.command()
def shell() -> None:
    from IPython import start_ipython

    start_ipython(argv=[])
