from collections import deque
import time


def is_valid(x, y, visited, rows, cols):
    return 0 <= x < rows and 0 <= y < cols and not visited[x][y]


def bfs(image, x, y, visited, rows, cols):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, visited, rows, cols) and image[new_x][new_y] == 1:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True
                size += 1

    return size


def find_largest_cloud_size(image):
    if not image:
        return 0

    rows, cols = len(image), len(image[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    largest_cloud_size = 0

    start_time = time.time()  # Record the start time

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and image[i][j] == 1:
                cloud_size = bfs(image, i, j, visited, rows, cols)
                largest_cloud_size = max(largest_cloud_size, cloud_size)

    end_time = time.time()  # Record the end time

    print("Size of the largest cloud:", largest_cloud_size)
    print("Running time:", end_time - start_time, "seconds")


# Example usage:
if __name__ == "__main__":
    M, N = map(int, input().split())
    image = [list(map(int, input().split())) for _ in range(M)]
    find_largest_cloud_size(image)
