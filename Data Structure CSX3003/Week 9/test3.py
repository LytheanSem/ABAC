adjacency_list = {}

# Initialize a set to store all unique nodes
nodes = set()

# Input the edge list interactively
print("Enter the edge list (node1 node2), one edge per line. Type 'done' to finish:")
while True:
    edge = input()
    if edge.lower() == 'done':
        break

    node1, node2 = edge.split()

    # Add nodes to the set of all nodes
    nodes.add(node1)
    nodes.add(node2)

    # Add edges to the adjacency list (undirected graph)
    if node1 in adjacency_list:
        adjacency_list[node1].append(node2)
    else:
        adjacency_list[node1] = [node2]

    if node2 in adjacency_list:
        adjacency_list[node2].append(node1)
    else:
        adjacency_list[node2] = [node1]

# Sort the adjacency list by node names
for node in adjacency_list:
    adjacency_list[node].sort()

# Create the adjacency matrix
num_nodes = len(nodes)
adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

node_index = {node: i for i, node in enumerate(sorted(nodes))}

for node, neighbors in adjacency_list.items():
    for neighbor in neighbors:
        adjacency_matrix[node_index[node]][node_index[neighbor]] = 1

print("Adjacency List:")
for node, neighbors in adjacency_list.items():
    print(f"{node} -> {', '.join(neighbors)}")

print("\nAdjacency Matrix:")
for row in adjacency_matrix:
    print(' '.join(map(str, row)))
