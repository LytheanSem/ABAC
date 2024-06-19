

def toAdjLists(M, V):
    # returns collection of adjacency lists
    # Complete this function!

    


def printAdjLists(A):
    i = 0
    for l in A:
        print(i, l)
        i += 1

V = int(input())
M = []
for i in range(V):
    aRow = list(map(int, input().split()))
    M.append(aRow)
adjLists = toAdjLists(M, V)
printAdjLists(adjLists)
    

    
