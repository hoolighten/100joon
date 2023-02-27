import sys
from collections import deque

def bfs(size_m, size_n, size_h):
    queue = deque()
    for rz in range(size_h):
        for ry in range(size_n):
            for rx in range(size_m):
                if graph[rz][ry][rx] == 1:
                    queue.append((rz, ry, rx))
    while queue:
        rz, ry, rx = queue.popleft()
        for i in range(6):
            nx = rx + dx[i]
            ny = ry + dy[i]
            nz = rz + dz[i]
            if 0 <= nx < size_m and 0 <= ny < size_n and 0 <= nz < size_h and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[rz][ry][rx] + 1
                queue.append((nz, ny, nx))
    day = 0
    for i in graph:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    exit(0)
            day = max(day, max(j))
    print(day-1)


input = sys.stdin.readline
m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for i in range(h)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
bfs(m, n, h)
