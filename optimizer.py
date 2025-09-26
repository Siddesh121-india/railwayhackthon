
import networkx as nx
import json

class RailwayOptimizer:
    def __init__(self, network_file):
        self.graph = nx.Graph()
        self.load_network(network_file)

    def load_network(self, file):
        with open(file) as f:
            data = json.load(f)
            for edge in data["edges"]:
                self.graph.add_edge(edge["from"], edge["to"], weight=edge["distance"])

    def get_shortest_path(self, start, end):
        try:
            path = nx.dijkstra_path(self.graph, start, end)
            distance = nx.dijkstra_path_length(self.graph, start, end)
            return {"path": path, "distance": distance}
        except Exception:
            return {"error": "No path found"}

    def get_stations(self):
        return list(self.graph.nodes)
