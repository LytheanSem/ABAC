# Directions for movement: up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Target solved state
target = '123456780'

# Convert the board to a string for easy comparison
def board_to_str(board):
    return ''.join(map(str, board))

# BFS algorithm using a regular list for the queue
def bfs(start):
    queue = [(start, start.index('0'), 0)]  # (current state, index of zero, depth)
    visited = {start}  # Set to keep track of visited states
    head = 0  # Used to simulate dequeuing from the list
    
    while head < len(queue):
        state, zero_idx, depth = queue[head]
        head += 1
        
        if state == target:
            return depth
        
        # Convert 1D index to 2D coordinates
        x, y = divmod(zero_idx, 3)
        
        # Try all possible moves
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            # Check if new coordinates are within bounds
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                # Swap the zero tile with the adjacent tile
                new_idx = new_x * 3 + new_y
                new_state = list(state)
                new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
                new_state_str = ''.join(new_state)
                
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, new_idx, depth + 1))

    return -1  # Should never reach here since a solution is guaranteed

# Input the puzzle
initial_state = []
for _ in range(3):
    initial_state.extend(list(map(str, input().split())))

# Run BFS and print the result
start_state = board_to_str(initial_state)
print(bfs(start_state))