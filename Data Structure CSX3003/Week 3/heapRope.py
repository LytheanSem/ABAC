import time


def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def connect_ropes(ropes):

    build_heap(ropes)

    cost = 0

    while len(ropes) > 1:

        smallest1 = ropes[0]
        ropes[0] = ropes[-1]
        ropes.pop()
        heapify(ropes, len(ropes), 0)

        smallest2 = ropes[0]
        ropes[0] = ropes[-1]
        ropes.pop()
        heapify(ropes, len(ropes), 0)

        new_rope = smallest1 + smallest2

        cost += new_rope

        ropes.append(new_rope)
        heapify(ropes, len(ropes), len(ropes) - 1)

    return cost


ropes = list(map(int, input().split()))
st = time.process_time()
minimum_cost = connect_ropes(ropes)
et = time.process_time()
print("Minimum cost to connect the ropes:", minimum_cost)
print(f"time: {et-st}")
