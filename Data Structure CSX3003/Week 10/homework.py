n = int(input())

G = []
G.append([])
for i in range(n):
    v = list(map(int, input().split()))
    G.append(v[2:])

q = []
q.append(1)

checked = [False] * (n + 1)
checked[1] = True
d = [-1] * (n + 1)
d[1] = 0

while q:
    current = q.pop(0)
    for v in G[current]:
        if not checked[v]:
            q.append(v)
            d[v] = d[current] + 1
            checked[v] = True

for i in range(1, n + 1):
    print(i, d[i])
