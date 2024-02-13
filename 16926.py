import sys
import copy


input = sys.stdin.readline

def rotation(x, y):
    data = graph[y][x]
    for _ in range(height-1):
        next_data = graph[y+1][x]
        graph[y+1][x] = data
        data = next_data
        y += 1
    for _ in range(length-1):
        next_data = graph[y][x+1]
        graph[y][x+1] = data
        data = next_data
        x += 1
    for _ in range(height-1):
        next_data = graph[y-1][x]
        graph[y-1][x] = data
        data = next_data
        y -= 1
    for _ in range(length-1):
        next_data = graph[y][x-1]
        graph[y][x-1] = data
        data = next_data
        x -= 1
    

n, m, r = map(int, input().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(r):
    start_x, start_y = 0, 0
    height, length = n, m
    for _ in range(min(n, m) // 2):
        rotation(start_x, start_y)
        start_x += 1
        start_y += 1
        height -= 2
        length -= 2
for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()
