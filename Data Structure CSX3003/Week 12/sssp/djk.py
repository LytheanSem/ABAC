from Heap import heap


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        pq = heap()

        pq.insert((0, src))  # Insert the start vertex with distance 0

        while not pq.empty():
            distance, u = pq.extract()  # Call extract on the Heap object

            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    pq.insert((dist[v], v))

        return dist


# Read input
n, m = map(int, input().split())
g = Graph(n)

for _ in range(m):
    u, v, w = map(int, input().split())
    g.add_edge(u - 1, v - 1, w)

# Assuming vertex 1 is the source
source = 0
distances = g.dijkstra(source)

# Print the distances from source to all vertices
for i, distance in enumerate(distances):
    print(f"Distance from vertex {source + 1} to vertex {i + 1}: {distance}")
