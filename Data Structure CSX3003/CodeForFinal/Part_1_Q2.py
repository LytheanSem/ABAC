
class DisjointSets:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0]*n

    def findset(self, u):
        if self.p[u] == u:
            return u
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]

    def union(self, u, v):
        a = self.findset(u)
        b = self.findset(v)
        if self.rank[a] < self.rank[b]:
            self.p[a] = b
        else:
            self.p[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1


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
    print("YES")
else:
    print("NO")
