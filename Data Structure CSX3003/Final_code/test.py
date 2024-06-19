# A class to represent a graph object

class Graph:

    def __init__(self, edges, n):

        # A list of lists to represent an adjacency list

        self.adjList = [[] for _ in range(n)]

        # add edges to the directed graph

        for (src, dest) in edges:

            self.adjList[src].append(dest)


# Function to perform DFS traversal on the graph on a graph

def DFS(graph, v, discovered, arrival, departure, time):

    time = time + 1

    # set the arrival time of vertex `v`

    arrival[v] = time

    # mark vertex as discovered

    discovered[v] = True

    for i in graph.adjList[v]:

        if not discovered[i]:

            time = DFS(graph, i, discovered, arrival, departure, time)

    time = time + 1

    # set departure time of vertex `v`

    departure[v] = time

    return time


if __name__ == '__main__':

    # List of graph edges as per the above diagram

    # edges = [(0, 1), (0, 2), (2, 3), (2, 4), (3, 1), (3, 5), (4, 5), (6, 7)]
    edges = [(1, 2), (1, 3), (7, 1), (7, 3), (2, 7), (4, 2),
             (3, 4), (6, 4), (4, 5), (5, 6), (5, 8)]
    # total number of nodes in the graph (labelled from 0 to 7)

    n = 11

    # build a graph from the given edges

    graph = Graph(edges, n)

    # list to store the arrival time of vertex

    arrival = [None] * n

    # list to store the departure time of vertex

    departure = [None] * n

    # mark all the vertices as not discovered

    discovered = [False] * n

    time = -1

    # Perform DFS traversal from all undiscovered nodes to

    # cover all unconnected components of a graph

    for i in range(n):

        if not discovered[i]:

            time = DFS(graph, i, discovered, arrival, departure, time)

    # print arrival and departure time of each vertex in DFS

    for i in range(n):

        print(f'Vertex {i}', (arrival[i], departure[i]))
