from disjointsets3 import DisjointSets
V, E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))


s = DisjointSets(V)


for edge in edgeList:
    u = edge[0]
    v = edge[1]
    s.union(u, v)

if len(set(s.findset(i) for i in range(V))) == 1:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
