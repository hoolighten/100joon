import sys
from collections import deque

def bfs(grid_x, grid_y):
    global graph
    queue = deque()
    queue.append((grid_y, grid_x))
    while queue:
        grid_x, grid_y = queue.popleft()
        for direction in range(4):
            nx = grid_x + dx[direction]
            ny = grid_y + dy[direction]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[grid_y][grid_x] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]




input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x, y = 0, 0
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

print(bfs(x, y))