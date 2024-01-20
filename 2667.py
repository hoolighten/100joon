import sys
from collections import deque

def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    graph[y][x] = 2
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 2
                cnt +=1
                queue.append((nx, ny))
    return cnt
                

input = sys.stdin.readline
n = int(input())
graph = list()
answer = list()
danji_cnt = 0
cnt = 1
answer = list()
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
for i in range(n):
    for j in range(n):
        if graph[j][i] == 1:
            danji_cnt +=1
            bfs(i, j)
            answer.append(cnt)
            cnt = 1
            
print(danji_cnt)
answer.sort()
for _ in answer:
    print(_)
