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


def mergesort(A, p, r):
    if p < r:
        q = (p+r)//2
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)
        print(A[p:r+1])


A = [52, 37, 63, 14, 17, 8, 6, 25]
n = len(A)
mergesort(A, 0, n-1)
