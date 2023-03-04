import sys
from collections import deque


def shark_eat(x_start, y_start, size):
    queue = deque([])
    queue.append([x_start, y_start])
    visited = [[0] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    visited[x_start][y_start] = 1
    temp = []
    while queue:
        x_start, y_start = queue.popleft()
        for k in range(4):
            nx = x_start + dx[k]
            ny = y_start + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] <= size:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x_start][y_start] + 1
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))


n = int(input())
graph = []
shark_size = 2
shark_hungry = 0
cnt = 0
result = 0
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x = i
            shark_y = j
while True:
    shark = shark_eat(shark_x, shark_y, shark_size)
    if len(shark) == 0:
        break
    ax, ay, dist = shark.pop()
    result += dist
    graph[shark_x][shark_y], graph[ax][ay] = 0, 0
    shark_x, shark_y = ax, ay
    cnt += 1
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
print(result)


