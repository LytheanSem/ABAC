import time
from Heap import heap


A = list(map(int, input().split()))

n = len(A)


def findMax(x, y):
    return x > y


def checkoutMax(a, lastIndex=0):
    # Locate the position of max item
    # Replace the item at max position with the last item
    # Return value of max item

    global h

    maxItem = h.extract()
    '''
    maxIndex = 0
    for i in range(1, lastIndex+1):
        if a[i] > a[maxIndex]:
            maxIndex = i
    maxItem = a[maxIndex]
    a[maxIndex] = a[lastIndex]
    '''
    return maxItem


st = time.process_time()

h = heap(A, findMax)
for i in range(n-1, -1, -1):
    A[i] = checkoutMax(A, i)

print(A)
et = time.process_time()
print(f"Time running: {et-st}")
