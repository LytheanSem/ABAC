def create_adjacency_lists(vertices, edge_list):
    adjacency_lists = [[] for _ in range(vertices)]

    for edge in edge_list:
        vertex1, vertex2 = edge
        adjacency_lists[vertex1].append(vertex2)
        adjacency_lists[vertex2].append(vertex1)

    return adjacency_lists


def print_adjacency_lists(adjacency_lists):
    for vertex, neighbors in enumerate(adjacency_lists):
        print(f"Vertex {vertex}: {neighbors}")


def main():
    vertices, edges = map(int, input().split())

    edge_list = []
    for _ in range(edges):
        vertex1, vertex2 = map(int, input().split())
        edge_list.append((vertex1, vertex2))

    adjacency_lists = create_adjacency_lists(vertices, edge_list)
    print("\nThe adjacency lists:")
    print_adjacency_lists(adjacency_lists)


if __name__ == "__main__":
    main()
