import sys
from collections import deque


def make_Wall(lab_map, cnt):
    if cnt == 4:
        return 0
    for i in range(n):
        for j in range(m):
            if lab_map[i][j] != 0:
                continue
            else:
                lab_map[i][j] = 1
                cnt +=1
                return make_Wall(lab_map, cnt)

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
direction_x = [0, 0, -1, 1]
direction_y = [1, -1, 0, 0]
queue = deque()

make_Wall(graph, 1)
for x in range(n):
    for y in range(m):
        if graph[x][y] == 2:
            queue.append((x, y))
while queue:
    virus_x, virus_y = queue.popleft()
    for i in range(4):
        virus_x = virus_x + direction_x[i]
        virus_y = virus_y + direction_y[i]
        if graph[virus_x][virus_y] == 0 and 0 <= virus_x < n and 0 <= virus_y < m:
            graph[virus_x][virus_y] == 2
            queue.append((virus_x, virus_y))


