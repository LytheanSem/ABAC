
import time

a = list(map(int, input().split()))

n = len(a)

# st = time.process_time()


def InsertionSort(a):

    # traversing the array from 1 to length of the array(a)
    for i in range(1, n):

        temp = a[i]

        # Shift elements of array[0 to i-1], that are
        # greater than temp, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and temp < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp


st = time.process_time()
InsertionSort(a)
et = time.process_time()
print(et-st)
