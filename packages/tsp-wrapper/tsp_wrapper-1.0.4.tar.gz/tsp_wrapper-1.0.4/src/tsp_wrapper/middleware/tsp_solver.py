from dataclasses import dataclass

from tsp_wrapper.tsp import factory

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


@dataclass
class TSPSolverMiddleware:
    def return_solution(self, manager, routing, solution, data):
        result = list()
        index = routing.Start(0)
        route_distance = 0
        while not routing.IsEnd(index):
            result.append(data[manager.IndexToNode(index)].name)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        result.append(data[manager.IndexToNode(index)].name)
        return result

    def convert(self, data: dict) -> dict:
        # Instantiate the data problem.

        # Create the routing index manager.
        manager = pywrapcp.RoutingIndexManager(len(data["locations"]), data["num_vehicles"], data["depot"])

        # Create Routing Model.
        routing = pywrapcp.RoutingModel(manager)

        distance_matrix = data["distances"]

        def distance_callback(from_index, to_index):
            """Returns the distance between the two nodes."""
            # Convert from routing variable Index to distance matrix NodeIndex.
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return distance_matrix[from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)

        # Define cost of each arc.
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

        # Solve the problem.
        solution = routing.SolveWithParameters(search_parameters)

        result: dict = {"id": data.get("id"), "locations": []}

        if solution:
            result["locations"] = (self.return_solution(manager, routing, solution, data["cities"]),)
        return result


def register() -> None:
    factory.register("tsp_solver", TSPSolverMiddleware)
