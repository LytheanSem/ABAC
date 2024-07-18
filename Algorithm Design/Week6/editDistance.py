import time
import sys
sys.setrecursionlimit(10000)  

A = input()
B = input()

memo = [[-1 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

def EditDistance(i, j):
    global A, B, memo

    # Check if result is already computed
    if memo[i][j] != -1:
        return memo[i][j]

    # If we reach the end of one string
    if i == len(A):
        return len(B) - j
    elif j == len(B):
        return len(A) - i

    # If the characters match, move to the next character in both strings
    elif A[i] == B[j]:
        answer = EditDistance(i + 1, j + 1)
    else:
        # Calculate cost for delete, insert, and substitute operations
        delete = 1 + EditDistance(i + 1, j)
        insert = 1 + EditDistance(i, j + 1)
        substitute = 1 + EditDistance(i + 1, j + 1)
        answer = min(delete, insert, substitute)

    # Save the computed result
    memo[i][j] = answer
    return answer

# Measure execution time
st = time.process_time()
print(EditDistance(0, 0))
et = time.process_time()
print(f"Running Time: {et - st}")


'''
import sys
sys.setrecursionlimit(10000)

A = input()
B = input()

def edist(i, j):
    if i == len(A) and j == len(B):
        return 0
    elif i == len(A) and j < len(B):
        return len(B) - j
    elif i < len(A) and j == len(B):
        return len(A) - i
    else:
        if A[i] == B[j]:
            return edist(i+1, j+1)
        else:
            ins = 1 + edist(i, j+1)
            dlt = 1 + edist(i+1, j)
            chg = 1 + edist(i+1, j+1)
            return min(ins, dlt, chg)
        

print(edist(0,0))
'''

'''
import sys
sys.setrecursionlimit(10000)

A = input()
B = input()

mm = {}

def edist(i, j):
    if mm.get((i,j)) == None:
        if i == len(A) and j == len(B):
            mm[(i,j)] = 0
        elif i == len(A) and j < len(B):
            mm[(i,j)] = len(B) - j
        elif i < len(A) and j == len(B):
            mm[(i,j)] = len(A) - i
        else:
            if A[i] == B[j]:
                mm[(i,j)] = edist(i+1, j+1)
            else:
                ins = 1 + edist(i, j+1)
                dlt = 1 + edist(i+1, j)
                chg = 1 + edist(i+1, j+1)
                mm[(i,j)] = min(ins, dlt, chg)
    return mm[(i,j)]

print(edist(0,0))
'''

'''
import sys
sys.setrecursionlimit(10000)

A = input()
B = input()

mm = [[-1]*(len(B)+1) for i in range(len(A)+1)]

def edist(i, j):
    if mm[i][j] == -1:
        if i == len(A) and j == len(B):
            mm[i][j] = 0
        elif i == len(A) and j < len(B):
            mm[i][j] = len(B) - j
        elif i < len(A) and j == len(B):
            mm[i][j] = len(A) - i
        else:
            if A[i] == B[j]:
                mm[i][j] = edist(i+1, j+1)
            else:
                ins = 1 + edist(i, j+1)
                dlt = 1 + edist(i+1, j)
                chg = 1 + edist(i+1, j+1)
                mm[i][j] = min(ins, dlt, chg)
    return mm[i][j]

print(edist(0,0))
'''