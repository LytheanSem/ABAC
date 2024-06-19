def partition(p, r):
    # Sample partition function, can be replaced with a valid implementation
    global A
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(p, r):
    global A
    if p < r:
        q = partition(p, r)
        print(A[p:q], A[q], A[q+1:r+1])  # Printing the partitioned elements
        quicksort(p, q - 1)
        quicksort(q + 1, r)


A = [52, 37, 63, 14, 17, 8, 6, 25]
quicksort(0, len(A) - 1)
