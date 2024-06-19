import sys
from Heap import *

V, E = map(int, input().split())
adj_list = [[] for v in range(V)]
for i in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
    # IMPORTANT: Prim's require 2 way connection representation
    adj_list[v].append((u, w))

print(adj_list)


class HeapNode():
    def __init__(self, vertex=None, key=sys.maxsize, parent=None):
        self.key = key
        self.parent = parent
        self.vertex = vertex


def PrimMST(r):
    MST = [False] * V
    MinKey = [sys.maxsize] * V
    total = 0

    s = HeapNode(r, 0, None)
    PQ = heap(cmp=lambda x, y: x.key < y.key)
    PQ.insert(s)
    while not PQ.empty():
        t = PQ.extract()
        u = t.vertex
        if not MST[u]:
            total += t.key
            MST[u] = True
            for v, w in adj_list[u]:
                if not MST[v] and w < MinKey[v]:
                    s = HeapNode(v, w, u)
                    MinKey[v] = w
                    PQ.insert(s)

    return MinKey, total


print(PrimMST(0))
