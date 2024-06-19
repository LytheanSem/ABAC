import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
        self.graph[u][v] = w

    def dijkstra(self, start_node):
        distances = {node: float('inf') for node in self.graph}
        distances[start_node] = 0
        previous = {node: None for node in self.graph}
        visited = set()

        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        self.print_shortest_paths(start_node, distances, previous)

    def print_shortest_paths(self, start_node, distances, previous):
        for node in self.graph:
            if node != start_node:
                path = self.get_shortest_path(start_node, node, previous)
                print(
                    f"Shortest path from {start_node} to {node}: {path}, Distance: {distances[node]}")

    def get_shortest_path(self, start_node, end_node, previous):
        path = []
        current_node = end_node
        while current_node is not None:
            path.insert(0, current_node)
            current_node = previous[current_node]
        return " -> ".join(path)


# Example usage:
g = Graph()
g.add_edge('0', '1', 4)
g.add_edge('0', '7', 8)
g.add_edge('1', '7', 11)
g.add_edge('1', '2', 8)
g.add_edge('7', '8', 7)
g.add_edge('7', '6', 1)
g.add_edge('2', '8', 2)
g.add_edge('2', '5', 4)
g.add_edge('2', '3', 7)
g.add_edge('8', '6', 6)
g.add_edge('6', '5', 2)
g.add_edge('5', '3', 14)
g.add_edge('5', '4', 10)
g.add_edge('3', '4', 9)

start_node = '0'
g.dijkstra(start_node)
