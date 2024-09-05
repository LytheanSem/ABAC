class DisjointSets:
    def __init__(self, n):
        self.p = list(range(n))  # parent pointers
        self.rank = [0] * n      # rank (tree height)
 
    def findset(self, u):
        if self.p[u] != u:
            self.p[u] = self.findset(self.p[u])  # path compression
        return self.p[u]
 
    def union(self, u, v):
        root_u = self.findset(u)
        root_v = self.findset(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.p[root_u] = root_v
                print(f"Union({u}, {v}): Root of {u} becomes {root_v}")
            elif self.rank[root_v] < self.rank[root_u]:
                self.p[root_v] = root_u
                print(f"Union({u}, {v}): Root of {v} becomes {root_u}")
            else:
                self.p[root_v] = root_u
                self.rank[root_u] += 1
                print(f"Union({u}, {v}): Roots are equal, {root_v} becomes child of {root_u}, rank of {root_u} increases")
 
def kruskal(V, edges):
    # Step 3: Sort edges by increasing order of weight
    edges.sort(key=lambda x: x[2])
   
    print("Sorted edges by weight:", edges)
   
    # Initialize DisjointSets for V vertices
    ds = DisjointSets(V)
   
    mst_weight = 0  # Store the total weight of MST
    mst_edges = []  # Store the edges included in the MST
 
    # Step 5: Iterate over sorted edges and apply Kruskal's algorithm
    for u, v, weight in edges:
        set_u = ds.findset(u)
        set_v = ds.findset(v)
        print(f"Processing edge ({u}, {v}, {weight}): Set of {u} is {set_u}, Set of {v} is {set_v}")
 
        if set_u != set_v:
            ds.union(u, v)
            mst_edges.append((u, v, weight))
            mst_weight += weight
            print(f"Edge ({u}, {v}, {weight}) added to the MST")
 
            # If we have added V-1 edges, stop (we have our MST)
            if len(mst_edges) == V - 1:
                break
 
    print("\nFinal MST:", mst_edges)
    print("Total weight of MST:", mst_weight)
    return mst_weight
 
# Input reading (number of vertices V and edges E, followed by edge list)
if __name__ == "__main__":
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]
 
    # Output the total weight of the minimum spanning tree
    kruskal(V, edges)

'''
# example

djs = DisjointSets(5)
for i in range(5):
    print(djs.findset(i))

djs.union(3,4)
print(djs.findset(3), djs.findset(4))

djs.union(4,1)
print(djs.findset(4), djs.findset(1))

'''
