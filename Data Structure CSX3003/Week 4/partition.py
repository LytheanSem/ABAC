
def partition(A, p, r):  # Lomuto's partition scheme
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i+1] = A[i+1], A[r]
    return i+1


A = list(map(int, input().split()))
size = len(A)
print(partition(A, 0, size-1))


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)  # left
        quicksort(A, q+1, r)  # right
