# A class to represent a graph object

class Graph:

    def __init__(self, edges, n):

        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]
        # Create a mapping between node labels and integers
        self.node_to_int = {}
        self.int_to_node = {}
        current_node = 0

        for (src, dest) in edges:
            if src not in self.node_to_int:
                self.node_to_int[src] = current_node
                self.int_to_node[current_node] = src
                current_node += 1
            if dest not in self.node_to_int:
                self.node_to_int[dest] = current_node
                self.int_to_node[current_node] = dest
                current_node += 1

            self.adjList[self.node_to_int[src]].append(self.node_to_int[dest])


# Function to perform DFS traversal on the graph

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

    edges = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "F"), ("C", "E"), ("D", "J"),
             ("D", "I"), ("E", "F"), ("F", "G"), ("G", "E"), ("H", "I"), ("H", "K"), ("I", "J"), ("J", "K"), ("K", "I")]

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
        print(f'Vertex {graph.int_to_node[i]}', (arrival[i], departure[i]))
