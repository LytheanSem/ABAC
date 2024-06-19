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
        self.graph[v][u] = w  # Since it's an undirected graph

    def prim_mst(self):
        key = {node: float('inf') for node in self.graph}
        parent = {node: None for node in self.graph}
        # Start from the first node in the graph
        start_node = list(self.graph.keys())[0]
        key[start_node] = 0
        mst_set = set()

        for _ in range(len(self.graph)):
            u = self.min_key(key, mst_set)
            mst_set.add(u)
            for v in self.graph[u]:
                if v not in mst_set and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

    def min_key(self, key, mst_set):
        min_val = float('inf')
        min_node = None
        for node in key:
            if node not in mst_set and key[node] < min_val:
                min_val = key[node]
                min_node = node
        return min_node

    def print_mst(self, parent):
        print("Edge \tWeight")
        for node in self.graph:
            if parent[node] is not None:
                print(parent[node], "-", node, "\t",
                      self.graph[node][parent[node]])


# Example usage:
g = Graph()
g.add_edge('A', 'B', 2)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 4)
g.add_edge('D', 'E', 4)

g.prim_mst()
