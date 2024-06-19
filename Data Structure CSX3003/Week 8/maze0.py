
# relative distance of above, below, left, and right cells
adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def valid(r, c):
    # return True if coordinate (r,c) is not outside the matrix
    # and is not a part of a wall

    global steps

    if r >= 0 and r < 10 and c >= 0 and c < 10:
        if steps[r][c] == 0:
            return True
    return False


'''
maze:  the input maze
ends:  the list of source and destination coordinates
steps: matrix that stores the minimum number of steps from
       the source coordinate to each visited maze cell.
       = -1 if the cell is part of a wall.
'''

# Read input maze
maze = []
ends = []
for r in range(10):
    maze.append(input())
print(maze)

# Set up the steps matrix
steps = [[0]*10 for r in range(10)]
for r in range(10):
    for c in range(10):
        if maze[r][c] == '#':
            steps[r][c] = -1
        if maze[r][c] == 'X':
            ends.append((r, c))

# Breadth-First Search
Queue = []
Queue.append((ends[0], 0))
while Queue != []:
    (r, c), step = Queue.pop(0)  # Dequeue from the front of the queue

    if (r, c) == ends[1]:
        print(step)  # Print the number of steps when destination is reached
        break

    for dr, dc in adj:
        new_r, new_c = r + dr, c + dc
        if valid(new_r, new_c):
            Queue.append(((new_r, new_c), step + 1))
            steps[new_r][new_c] = step + 1
