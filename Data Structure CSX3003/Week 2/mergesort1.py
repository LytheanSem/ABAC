
import time


def merge(A, p, q, r):
    B = []
    i = p
    j = q+1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    A[p:r+1] = B + A[i:q+1] + A[j:r+1]


def mergesort(a, p, r):
    if p < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = p+(r-p)//2

        # Sort first and second halves
        mergesort(a, p, m)
        mergesort(a, m+1, r)
        merge(a, p, m, r)


a = list(map(int, input().split()))


st = time.process_time()

mergesort(a, 0, len(a)-1)

et = time.process_time()

print(a)
print(et-st)
