import time
 
# Accepting number of activities from the user
N = int(input("Enter the number of activities: "))
 
# List to hold the start and finish times of activities
Activities = []
 
# Accepting start and finish times for each activity
print(f"Enter the start and finish times for {N} activities (each as two space-separated integers):")
for _ in range(N):
    Activities.append(tuple(map(int, input().split())))
 
def ActivitySelection(n, Activities):
    # Sort the activities based on finish times in ascending order
    Activities.sort(key=lambda x: x[1])
 
    # Always select the first activity
    count = 1
    left = 0
    print(f"Selected Activity: {Activities[left]}")  # Print the first selected activity
   
    # Iterate through the remaining activities
    for right in range(1, n):
        # Select activity if it starts after the last selected activity finishes
        if Activities[left][1] < Activities[right][0]:
            print(f"Selected Activity: {Activities[right]}")  # Print the selected activity
            count += 1
            left = right  # Update the last selected activity index
   
    # Print the total number of selected activities
    print("Total selected activities:", count)
 
# Measure and display the running time of the algorithm
st = time.process_time()
ActivitySelection(N, Activities)
et = time.process_time()
print(f"Running Time: {et-st} seconds")
 