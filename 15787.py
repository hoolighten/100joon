import sys

train_seat = []
n, m = map(int, input().split())
train_seat = [[0 for i in range(20)]for j in range(n)]
state = []
out = 0

for _ in range(m):
    order_list = list(map(int, input().split()))
    if order_list[0] == 1:
        if train_seat[order_list[1]-1][order_list[2]-1] == 0:
            train_seat[order_list[1]-1][order_list[2]-1] = 1
        else:
            continue
    if order_list[0] == 2:
        if train_seat[order_list[1]-1][order_list[2]-1] == 1:
            train_seat[order_list[1]-1][order_list[2]-1] = 0
        else:
            continue
    if order_list[0] == 3:
        for i in range(19, -1, -1):
            train_seat[order_list[1]-1][i] = train_seat[order_list[1]-1][i-1]
        train_seat[order_list[1]-1][0] = 0
    if order_list[0] == 4:
        for i in range(19):
            train_seat[order_list[1]-1][i] = train_seat[order_list[1]-1][i+1]
        train_seat[order_list[1]-1][19] = 0

for i in range(n):
    if train_seat[i] not in state:
        state.append(train_seat[i])
        out += 1
print(out)
