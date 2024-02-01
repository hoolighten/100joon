import sys
from collections import deque

r, c, n = map(int, input().split())
graph = list()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = list()
[['O' for i in range(c)] for j in range(r)]
def bomb(_graph):
    bomb_graph = [['O' for i in range(c)] for j in range(r)]
    for y in range(r):
        for x in range(c):
            if _graph[y][x] == 'O':
                bomb_graph[y][x] = '.'
                for k in range(4):
                    nx = dx[k] + x
                    ny = dy[k] + y
                    if nx < 0 or nx >= c or ny < 0 or ny >= r:
                        continue
                    bomb_graph[ny][nx] = '.'
    return bomb_graph
for _ in range(r):
    graph.append(input().rstrip())
_bomb = bomb(graph)
if n % 2 == 0:
    for i in range(r):
        answer.append(''.join([['O' for i in range(c)] for j in range(r)][i]))
if n % 4 == 3:
    for i in range(r):
        answer.append(''.join(_bomb[i]))
if n % 4 == 1:
    if n == 1:
        answer.append('\n'.join(graph))
    else:
        for i in range(r):
            answer.append(''.join((bomb(_bomb))[i]))
print('\n'.join(answer))
