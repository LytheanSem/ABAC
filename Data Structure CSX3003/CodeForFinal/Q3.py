class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)


def DFS(graph, v, discovered, arrival, departure, time):
    time = time + 1

    arrival[v] = time

    discovered[v] = True

    for i in graph.adjList[v]:
        if not discovered[i]:
            time = DFS(graph, i, discovered, arrival, departure, time)
    time = time + 1

    departure[v] = time

    return time


if __name__ == '__main__':
    edges = [(0, 1), (0, 2), (1, 3),
             (3, 5), (5, 4), (4, 3)]
    n = 6
    time = 0
    graph = Graph(edges, n)

    arrival = [None] * n

    departure = [None] * n

    discovered = [False] * n
    time -= 1

    for i in range(n):
        if not discovered[i]:
            time = DFS(graph, i, discovered, arrival, departure, time)

    for i in range(n):
        print(f"Vertex {i}", (arrival[i], departure[i]))
