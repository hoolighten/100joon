import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[y][x] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 0:
                answer_graph[ny][nx] = 0
                continue
            if visited[ny][nx] == False:
                answer_graph[ny][nx] = answer_graph[y][x] + 1
                visited[ny][nx] = True
                q.append((nx, ny))

input = sys.stdin.readline
n, m = map(int, input().split())
graph = list()
answer_graph = [[-1]*(m) for _ in range(n)]
visited = [[False for i in range(m)] for j in range(n)]
answer = list()
for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            answer_graph[i][j] = 0
            bfs(j, i)
        if graph[i][j] == 0 and answer_graph[i][j] == -1:
            answer_graph[i][j] = 0
for i in range(n):
    print(*answer_graph[i])
