def num_harvesters(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    memo[n] = num_harvesters(n-1, memo) + num_harvesters(n-2, memo)
    return memo[n]


n = int(input())
print(num_harvesters(n))