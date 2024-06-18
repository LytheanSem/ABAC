import time

def GFG(a, size):
    max_so_far = float('-inf')  
    # Use float('-inf') instead of maxint
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far
# Driver function to check the above function
a = list(map(int, input().split()))

start = time.process_time()
print("Maximum contiguous sum is", GFG(a, len(a)))
end = time.process_time()
print(f"time finished: {end-start}")