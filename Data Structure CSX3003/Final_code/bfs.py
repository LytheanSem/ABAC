graph_type = input()
V,E = map(int, input().split())
adj_list = [[] for v in range(V)]
for i in range(E):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)
    if graph_type == "Undirected Graph":
        adj_list[v].append(u)

color = ["WHITE"]*V
d = [-1]*V
p = [None]*V

# Write your Breast-First Search code below

s = 0
color[s] = "GRAY"
d[s] = 0
p[s] = None
Q = []
Q.append(s)

while Q != []:
    u = Q[0]
    del Q[0]
    for v in adj_list[u]:
        if color[v] == "WHITE":
            color[v] = "GRAY"
            d[v] = d[u] + 1
            p[v] = u
            Q.append(v)
    color[u] = "BLACK"



# The code below is for printing output

for v in range(V):
    if d[v] == -1:
        dv = "Inf"
    else:
        dv = d[v]
    if p[v] != None:
        pv = p[v]+1
    else:
        pv = "None"

    print("%d %5s" % (v+1, color[v]), dv, pv)

