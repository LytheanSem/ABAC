import numpy as np


inputMatrix = []
for _ in range(10):
    inputMatrix.append(list(input()))

for y in range(len(inputMatrix)):
    inputMatrix[y].insert(0,"#")
    inputMatrix[y].append("#")


border = ["#" for i in range(12)]
inputMatrix.insert(0,border)
inputMatrix.append(border)




distance = [[0 for i in range(12)] for i in range(12)]


startX, startY = -1, -1
for y in range(len(inputMatrix)):
    for x in range(len(inputMatrix[0])):
        if inputMatrix[y][x] == "X":
            startX, startY = x, y
            break


Q = []
inputMatrix[startY][startX] = "#"
distance[startY][startX] = 0
Q.append((startX, startY))


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
done = False
while Q and not done:
    point = Q[0]
    del Q[0]

    for direction in directions:
        x = point[0] + direction[0]
        y = point[1] + direction[1]
        d = distance[point[1]][point[0]] + 1
        if inputMatrix[y][x] == "X":
            print(d)
            done = True

        elif inputMatrix[y][x] != "#":
            inputMatrix[y][x] = "#"
            distance[y][x] = d
            Q.append((x, y))






