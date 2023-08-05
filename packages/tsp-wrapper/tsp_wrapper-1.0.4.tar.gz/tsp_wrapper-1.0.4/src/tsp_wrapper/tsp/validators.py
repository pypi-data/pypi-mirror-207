def validate_tsp_input(data):
    required_keys = ["locations", "num_vehicles", "depot", "id"]
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Key not found : {key !r}")
