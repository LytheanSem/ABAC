class DisjointSet:
    parent = {}

    def makeSet(self, n):
        for i in range(n):
            self.parent[i] = i

    def find(self, k):
        # if k is root
        if self.parent[k] == k:
            return k
        return self.find(self.parent[k])

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        self.parent[x] = y


def kurskals_algo(A, B):
    mst = []
    ds = DisjointSet()
    ds.makeSet(A)
    index = 0
    B.sort(key=lambda x: x[2])
    while len(mst) != A - 1:
        (src, dest, weight) = B[index]
        index = index + 1
        x = ds.find(src-1)
        y = ds.find(dest-1)
        if x != y:
            mst.append((src, dest, weight))
            ds.union(x, y)

    cost = sum([x[2] for x in mst])
    return cost
