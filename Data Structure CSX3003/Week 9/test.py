def create_adjacency_matrix(vertices, edge_list):
    # Initialize an empty adjacency matrix with all zeros
    adjacency_matrix = [[0] * vertices for _ in range(vertices)]

    # Populate the adjacency matrix based on the edge list
    for edge in edge_list:
        vertex1, vertex2 = edge
        adjacency_matrix[vertex1][vertex2] = 1
        adjacency_matrix[vertex2][vertex1] = 1

    return adjacency_matrix


def print_adjacency_matrix(adjacency_matrix):
    for row in adjacency_matrix:
        print(" ".join(str(val) for val in row))


def main():
    vertices, edges = map(int, input().split())

    edge_list = []
    for _ in range(edges):
        vertex1, vertex2 = map(int, input().split())
        edge_list.append((vertex1, vertex2))

    adjacency_matrix = create_adjacency_matrix(vertices, edge_list)
    print_adjacency_matrix(adjacency_matrix)


if __name__ == "__main__":
    main()
