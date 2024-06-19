class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def bellman_ford(self, src, dest):
        dist = [float("inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            relaxed = False
            for s, d, w in self.graph:
                if dist[s] != float("inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
                    relaxed = True
            if not relaxed:
                break

        for s, d, w in self.graph:
            if dist[s] != float("inf") and dist[s] + w < dist[d]:
                return "Graph contains negative weight cycle"

        return dist[dest]


V, E = map(int, input().split())
graph = Graph(V)

for _ in range(E):
    node1, node2, weight = map(int, input().split())
    graph.add_edge(node1 - 1, node2 - 1, weight)

src_vertex = 0
dest_vertex = V - 1


print(graph.bellman_ford(src_vertex, dest_vertex))
