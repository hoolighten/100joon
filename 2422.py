import sys

input = sys.stdin.readline


n, m = map(int, input().split())
mixed = [[]*(n+1)for _ in range(n+1)]
cnt = 0
for i in range(m):
    a, b = map(int, input().split())
    mixed[a].append(b)
    mixed[b].append(a)
for i in range(1, n+1):
    for j in range(i + 1, n+1):
        for k in range(j + 1, n+1):
            if j not in mixed[i] and k not in mixed[i] and k not in mixed[j]:
                cnt +=1
print(cnt)
