def binary_search(arr, item):
    low = 0
    high = len(arr) -1
    mid = 0
    
    while low<=high:
        mid = (low + high) // 2 #integer part
    
        if item == arr[mid]:
            return mid

        elif item < arr[mid]:
            high = mid - 1
        
        else:              # elif item > arr[mid]:
            low = mid + 1
    
    return -1
    
    
arr = [2,3,4,5,7,8,12] #only work with sorted list
item = 12
result = binary_search(arr, item)

if result != -1:
    print(f"Found at : {str(result)}")
else:
    print("Not in the array!!")