from collections import deque

def rail_move():
    u, d = up.pop(), down.popleft()
    down.append(u)
    up.appendleft(d)
    if up[n-1][2] == 1:
        up[n-1][2] = 0


def take_movingwalk():
    global chk
    if up[0][1] == 0 or up[0][2] == 1:
        return 0
    else:
        up[0][2] = 1
        up[0][1] -= 1

def people_move():
    global chk
    for i in range(n-2, -1, -1):
        if up[i+1][1] and up[i+1][2] == 0 and up[i][2]:
            up[i][2] = 0
            up[i+1][2] = 1
            up[i+1][1] -=1
        if up[n-1][2] == 1:
            up[n-1][2] = 0



# def move_end():
up = deque()
down = deque()
n, k = map(int, input().split())
rail_saftey = list(map(int, input().split()))
cnt = 0
people = []

for i in range(n):
    up.append([i+1, rail_saftey[i], 0])
for i in range(n, 2*n):
    down.appendleft([i+1, rail_saftey[i], 0])

for i in range(200):
    cnt +=1
    rail_move()
    # print('after rail move')
    # for i in range(n):
    #     print(up[i][2], '   ', up[i][1])
    # print('')
    people_move()
    # print('after a people move')
    # for i in range(n):
    #     print(up[i][2], '   ', up[i][1])
    # print('')
    take_movingwalk()
    # print('take a moving walk')
    # for i in range(n):
    #     print(up[i][2], '   ', up[i][1])
    # print('')
print(cnt)
