V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

k = int(input())

from disjointsets3 import DisjointSets

s = DisjointSets(V)
edgeList.sort(key = lambda a:a[2])

setCount = V
for u,v,w in edgeList:
    if s.findset(u) != s.findset(v):
        s.union(u,v)
        setCount -= 1

    if setCount == k:
        break

Gap = []
for u,v,w in edgeList:
    if s.findset(u) != s.findset(v):
        Gap.append(w)

print(Gap)
print(min(Gap))


