def is_valid(x, y, M, N):
    return 0 <= x < M and 0 <= y < N


def dfs(x, y, grid, visited):
    if not is_valid(x, y, M, N) or visited[x][y] or grid[x][y] == 0:
        return 0

    visited[x][y] = True
    size = 1

    # Explore neighbors in 4 directions (up, down, left, right)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        size += dfs(new_x, new_y, grid, visited)

    return size


def find_largest_cloud_size(M, N, grid):
    visited = [[False for _ in range(N)] for _ in range(M)]
    max_cloud_size = 0

    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1 and not visited[i][j]:
                cloud_size = dfs(i, j, grid, visited)
                max_cloud_size = max(max_cloud_size, cloud_size)

    return max_cloud_size


# Input
M, N = map(int, input().split())
grid = []
for _ in range(M):
    row = list(map(int, input().split()))
    grid.append(row)

print(grid)
# Find and print the size of the largest cloud
largest_cloud_size = find_largest_cloud_size(M, N, grid)
print(largest_cloud_size)
