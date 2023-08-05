BROKER_URL = "amqp://guest:guest@localhost:5672/"

INBOUND_QUEUE = "inbound"
OUTBOUND_QUEUE = "outbound"

EXCHANGE_NAME = "tasks"

MIDDLEWARE = [
    "tsp_wrapper.middleware.dict_to_city",
    "tsp_wrapper.middleware.euclidean_distance",
    "tsp_wrapper.middleware.tsp_solver",
]

# ORDER IS IMPORTANT
TSP_CONVERTER = [
    "city",
    "euclidean",
    "tsp_solver",
]
