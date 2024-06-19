from Heap import heap


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        min_cost = 0
        visited = [False] * self.V
        pq = heap()

        pq.insert((0, 0))  # Insert the start vertex with weight 0

        while not pq.empty():
            weight, u = pq.extract()
            if visited[u]:
                continue

            visited[u] = True
            min_cost += weight

            for v, w in self.graph[u]:
                if not visited[v]:
                    pq.insert((w, v))

        return min_cost


# Read input
n, m = map(int, input().split())
g = Graph(n)

for _ in range(m):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

min_cost = g.prim_mst()
print(min_cost)
