def minimum_watering_time(n, moisture):
    # Pair the moisture content with its index
    flowers = [(moisture[i], i) for i in range(n)]
    
    # Sort flowers based on moisture content, breaking ties by position
    flowers.sort()
    
    # Start at the first flower
    time = 0
    current_position = 0
    
    for _, pos in flowers:
        # Add the time to walk to the next flower
        time += abs(pos - current_position)
        # Water the flower (1 minute per flower)
        time += 1
        # Update current position
        current_position = pos
    
    return time

# Input reading
n = int(input())  # number of flowers
moisture = list(map(int, input().split()))  # moisture content of flowers

# Get the minimal time and print it
print(minimum_watering_time(n, moisture))