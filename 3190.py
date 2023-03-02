from collections import deque


def turn(_dir, arr):
    a, b, c, d = arr[0], arr[1], arr[2], arr[3]
    if _dir == "D":
        arr[0], arr[1], arr[2], arr[3] = b, c, d, a
    else:
        arr[0], arr[1], arr[2], arr[3] = b, c, d, a
    return arr


times = 1
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
    time, direction = input().split()
    time = int(time)
    for _ in range(time):
        nx = nx + dir_array[0][0]
        ny = ny + dir_array[0][1]
        # if nx < 0 or nx >= n or ny < 0 or ny >= n or snake_map[nx][ny] == 1:
        #     break
        if snake_map[nx][ny] == 0:
            x_tail, y_tail = queue.popleft()
            snake_map[x_tail][y_tail] = 0
        times += 1
        snake_map[nx][ny] = 1
        queue.append((nx, ny))
    dir_array = turn(direction, dir_array)
print(times)
