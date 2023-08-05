from tsp_wrapper.utils.decorators import task

from tsp_wrapper.tsp.factory import create
from tsp_wrapper.conf import TSP_CONVERTER
from tsp_wrapper.tsp.validators import validate_tsp_input


@task(validators=[validate_tsp_input])
def tsp_solver_task(data):
    # create the middlewares objs
    middlewares = [create(item) for item in TSP_CONVERTER]
    # running the middlewares like a chain
    for middleware in middlewares:
        data = middleware.convert(data)
    return data


def get_ans(res):
    print(res)
