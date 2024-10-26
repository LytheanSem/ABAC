N = int(input())
x = 0
if N >= 0:
    for i in range(0, N+1):
        x += i
else:
    for i in range(0, N-1, -1):
        x += i
print(x)
