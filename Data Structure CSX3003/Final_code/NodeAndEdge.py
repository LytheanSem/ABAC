import numpy as np

v1, v2, v3, v4, v5, v6 = range(6)
G1 = [[3, 1], [3, 2], [2, 3], [2, 1], [1, 3], [1, 2], [1, 0], [0, 1] ]
G2 = [["v1", "v2"]
    , ["v1", "v3"]
    , ["v3", "v2"]
    , ["v3", "v4"]
    , ["v4", "v3"]
      ]

G3 = [["v1", "v2"]
    , ["v1", "v3"]
    , ["v2", "v1"]
    , ["v2", "v3"]
    , ["v2", "v4"]
    , ["v2", "v5"]
    , ["v3", "v1"]
    , ["v3", "v2"]
    , ["v3", "v5"]
    , ["v4", "v2"]
    , ["v4", "v5"]
    , ["v4", "v6"]
    , ["v5", "v3"]
    , ["v5", "v2"]
    , ["v5", "v4"]
    , ["v5", "v6"]
    , ["v6", "v4"]
    , ["v6", "v5"]
      ]

A, B, D, F, N = range(5)
G4 = [["A", "B"]
    , ["B", "F"]
    , ["B", "D"]
    , ["F", "N"]
    , ["F", "A"]
    , ["N", "F"]
    , ["N", "B"]
    , ["D", "A"]
      ]

def ADJMatrixList(EdgeList):
    vertexList = []
    for i in range(len(EdgeList)):
        for j in range(2):
            vertexList.append(EdgeList[i][j])

    vertexList = list(set(vertexList))
    vertexList.sort()

    vertices = len(vertexList)



    ADJMatrix = [[0 for i in range(vertices)] for j in range(vertices)]
    for i,j in EdgeList:
        x = vertexList.index(i)
        y = vertexList.index(j)
        ADJMatrix[x][y] = 1


    ADJList = []
    for i in range(len(vertexList)):
        temp = [vertexList[i]]
        for edge in EdgeList:
            if edge[0] == vertexList[i]:
                temp.append(edge[1])

        ADJList.append(temp)


    print(np.array(ADJMatrix))
    print((ADJList))


ADJMatrixList(G1)
ADJMatrixList(G2)
ADJMatrixList(G3)
ADJMatrixList(G4)