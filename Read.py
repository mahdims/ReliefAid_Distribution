import json

class Data:
    def __init__(self, file_name):
        self.name = None
        self.numNodes = None
        self.vehicleCapacity = None
        self.totalSupplyAtDepot = None
        self.gamma = None
        self.shortestDistances = None
        self.nodeInfo = None
        self.maxTourLimit = None
        self.numVehicles = None
        self.totalTravelTimeEpsilon = None
        self.load_from_file(file_name)

    def load_from_file(self, file_name):
        with open(file_name, 'r') as f:
            data = json.load(f)

        self.name = data.get("Name")
        self.numNodes = data.get("Number_of_nodes")
        self.vehicleCapacity = data.get("Vehicle_capacity")
        self.totalSupplyAtDepot = data.get("Total_supply_at_depot")
        self.gamma = data.get("Gamma")
        self.shortestDistances = {eval(k): v for k, v in
                                  data.get("Shortest_distances", {}).items()}
        self.nodeInfo = data.get("Node_info")
        self.maxTourLimit = data.get("Maximum_tour_limit")
        self.numVehicles = data.get("Number_of_vehicles")
        self.totalTravelTimeEpsilon = data.get("Total_travel_time_epsilon")

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Number of Nodes including depot: {self.numNodes}\n"
            f"Vehicle Capacity: {self.vehicleCapacity}\n"
            f"Total Supply at Depot: {self.totalSupplyAtDepot}\n"
            f"Max Tour Limit: {self.maxTourLimit}\n"
            f"Number of Vehicles: {self.numVehicles}\n"
            f"Total Travel Time Epsilon: {self.totalTravelTimeEpsilon}\n"
            f"Distance Matrix Size: {len(self.shortestDistances)}"
        )


if __name__ == "__main__":
    dataSet = "Van"
    fileName = "Van15_A1.json"
    data = Data(f"./{dataSet}/{fileName}")
    print(data)
