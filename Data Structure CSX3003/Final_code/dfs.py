graph_type = input()
if graph_type != "Directed Graph":
    print("DFS only works on Directed Graph")
    exit()

V,E = map(int, input().split())
adj_list = [[] for v in range(V)]
for i in range(E):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)



# Write your Depth-First Search code below
# Don't forget to make the initial dfs call! :)
def dfs_visit(u):
    global time
    time = time + 1
    d[u] = time
    color[u] = "GRAY"
    
    for v in adj_list[u]:
        if color[v] == "WHITE":
            p[v] = u
            dfs_visit(v)
    color[u] = "BLACK"
    time = time + 1
    f[u] = time
    
    
color = ["WHITE"]*V
p = [None]*V
time = 0
d = [-1]*V
f = [-1]*V
for u in range(V):
    if color[u] == "WHITE":
        dfs_visit(u)



# The code below is for printing output

for v in range(V):
    if d[v] == -1:
        dv = "undiscovered"
    else:
        dv = d[v]
    if f[v] == -1:
        fv = ""
    else:
        fv = f[v]
    if p[v] != None:
        pv = p[v]+1
    else:
        pv = "None"

    print("%d %5s" % (v+1, color[v]), dv, fv, pv)

