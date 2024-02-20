import sys
from collections import deque
input = sys.stdin.readline

def bfs(_x, _y, cnt):
    q = deque()
    q.append((_x, _y))
    while q:
        x, y = q.popleft()
        if y % 2 == 0:
            dx = dx_0
        else:
            dx = dx_1
        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < m+2 and 0 <= ny < n+2:
                if graph[ny][nx] == 1:
                    cnt +=1
                elif graph[ny][nx] == 0 and not visited[ny][nx]:
                    q.append((nx, ny))
                    visited[ny][nx] = True
    return cnt



m, n = map(int, input().split())
graph = [[0 for i in range(m+2)] for j in range(n+2)]
dx_1, dx_0, dy = [0, 1, 1, 1, 0, -1], [-1, 0, 1, 0, -1, -1], [-1, -1, 0, 1, 1, 0]
visited = [[False]*(m+2) for _ in range(n+2)]

for i in range(1,n+1):
    graph[i][1:m+1] = map(int, input().split())

ans = bfs(0, 0, 0)
print(ans)
