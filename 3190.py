from collections import deque


def turn(_dir, arr):
    a, b, c, d = arr[0], arr[1], arr[2], arr[3]
    if _dir == "D":
        arr[0], arr[1], arr[2], arr[3] = b, c, d, a
    else:
        arr[0], arr[1], arr[2], arr[3] = d, a, b, c
    return arr


info = []
times = 0
n = int(input())
dir_array = [[0, 1], [1, 0], [0, -1], [-1, 0]]
snake_map = [[0 for i in range(n)] for j in range(n)]
nx, ny = 0, 0
snake_map[0][0] = 1
k = int(input())
for _ in range(k):
    x_apple, y_apple = map(int, input().split())
    snake_map[x_apple - 1][y_apple - 1] = 2
queue = deque()
queue.append((0, 0))
l = int(input())
for _ in range(l):
    inf_turn = input().split()
    info.append([int(inf_turn[0]), inf_turn[1]])

while True:
    nx = nx + dir_array[0][0]
    ny = ny + dir_array[0][1]
    if 0 <= nx < n and 0 <= ny < n and snake_map[nx][ny] != 1:
        if snake_map[nx][ny] == 0:
            x_tail, y_tail = queue.popleft()
            snake_map[x_tail][y_tail] = 0
    else:
        break
    snake_map[nx][ny] = 1
    queue.append((nx, ny))
    times += 1
    for i in info:
        if times == i[0]:
            dir_array = turn(i[1], dir_array)
print(times + 1)
