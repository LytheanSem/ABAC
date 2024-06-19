graph_type = input()
V, E = map(int, input().split())
adj_list = [[] for v in range(V)]
for i in range(E):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)
    if graph_type == "Undirected Graph":
        adj_list[v].append(u)

color = ["WHITE"] * V
d = [-1] * V
p = [None] * V


def bfs(start):
    queue = []
    queue.append(start)
    color[start] = "GRAY"
    d[start] = 0
    p[start] = None

    print(queue)

    while queue:
        u = queue.pop(0)  # Equivalent to dequeuing the front element

        for v in adj_list[u]:
            if color[v] == "WHITE":
                color[v] = "GRAY"
                d[v] = d[u] + 1
                p[v] = u
                queue.append(v)  # Equivalent to enqueuing at the back

        color[u] = "BLACK"


for v in range(V):
    if color[v] == "WHITE":
        bfs(v)

for v in range(V):
    if d[v] == -1:
        dv = "Inf"
    else:
        dv = d[v]
    if p[v] is not None:
        pv = p[v] + 1
    else:
        pv = "None"

    print("%d %5s %2s %2s" % (v + 1, color[v], dv, pv))
