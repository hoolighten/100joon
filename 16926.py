import sys
import copy

def rotation(x, y):
    for _ in range(n-1):
        answer_graph[y+1][x] = graph[y][x]
        y += 1
        visited[y][x] = True
    for _ in range(m-1):
        answer_graph[y][x+1] = graph[y][x]
        x += 1
        visited[y][x] = True
    for _ in range(n-1):
        answer_graph[y-1][x] = graph[y][x]
        y -= 1
        visited[y][x] = True
    for _ in range(m-1):
        answer_graph[y][x-1] = graph[y][x]
        x -= 1
        visited[y][x] = True
    

input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = list()
visited = [[False]*m for i in range(n)]
start_x, start_y = 0, 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
answer_graph = copy.deepcopy(graph)
while visited[start_y][start_x] == False:
    for i in range(r):
        rotation(start_x, start_y)
        graph = copy.deepcopy(answer_graph)
    start_x += 1
    start_y += 1
    n -= 2
    m -= 2
print(answer_graph)
