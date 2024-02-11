import sys
from collections import deque

q = deque()
n, k = map(int, input().split())
stone = list(map(int, input().split()))
visited = [False]*n

q.append(0)
while q:
    start = q.popleft()
    for end in range(start + 1, n):
        if ((end - start) * (1 + abs(stone[end] - stone[start]))) <= k and not visited[end]:
            visited[end] = True
            q.append(end)
            if visited[n-1] == True:
                print("YES")
                sys.exit(0)
print("NO")
