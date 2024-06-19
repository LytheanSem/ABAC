from topological_sort import *
import numpy as np
n, e = map(int, input().split()) # n is number of vertices, e is number of edge
EdgeList = []
for i in range(e):
    x = list(map(int, input().split()))
    EdgeList.append(x)



vertexList = []
for i in range(len(EdgeList)):
    for j in range(2):
        vertexList.append(EdgeList[i][j])

vertexList = list(set(vertexList))
vertexList.sort()

vertices = len(vertexList)

ADJList = []
for i in range(len(vertexList)):
    temp = [vertexList[i]]
    for edge in EdgeList:
        if edge[0] == vertexList[i]:
            temp.append(edge[1])

    ADJList.append(temp)

result = topological_sort(len(vertexList),ADJList)


print(result)