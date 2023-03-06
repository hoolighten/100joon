def right_turn(direction):
    a, b, c, d = direction[0], direction[1], direction[2], direction[3]
    direction[0], direction[1], direction[2], direction[3] = d, a, b, c


n = int(input())
place = int(input())
break_p = 0
distance = 1
input_graph = [[0 for i in range(n)] for j in range(n)]
x_start, y_start = (n - 1) // 2, (n - 1) // 2
move_cnt = 1
direction_list = [[-1, 0], [0, -1], [1, 0], [0, 1]]
input_graph[x_start][y_start] = 1

while True:
    for _ in range(2):
        if break_p == 1:
            break
        for i in range(move_cnt):
            x_end = x_start + direction_list[0][0]
            y_end = y_start + direction_list[0][1]
            if x_end < 0 or x_end >= n or y_end < 0 or y_end >= n:
                break_p = 1
                break
            input_graph[x_end][y_end] = input_graph[x_start][y_start] + 1
            x_start = x_end
            y_start = y_end
            if input_graph[x_end][y_end] == place:
                x_axis, y_axis = x_end + 1, y_end + 1
        right_turn(direction_list)
    move_cnt += 1
    if break_p == 1:
        break
for i in input_graph:
    print(*i)
print(x_axis, y_axis)
