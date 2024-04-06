import sys



def growth_tree():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                tree_place.append([j, i])
    for j in range(len(tree_place)):
        x = tree_place[j][0]
        y = tree_place[j][1]
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] > 0:
                cnt += 1
        graph[y][x] += cnt



def seed():
    can_seed = 0
    for x, y in tree_place:
        before_seed = can_seed
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 0:
                can_seed += 1
                seed_axis.append([nx, ny])
        if can_seed == before_seed:
            continue
        new_tree = graph[y][x] // (can_seed - before_seed)
        for i in range(before_seed, can_seed):
            seed_axis[i].append(new_tree)
    for x, y, val in seed_axis:
        graph[y][x] += val

def namu_plus():
    for i in range(len(seed_axis)):
        tree_place.append([seed_axis[i][0], seed_axis[i][1]])


def find_destroy():
    max_val = 0
    destroy_x = -1
    destroy_y = - 1
    for i in range(len(tree_place)):
        x, y = tree_place[i][0], tree_place[i][1]
        if graph[y][x] == 0:
            continue
        val = graph[y][x]
        for direction in range(4):
            nx = x + dcx[direction]
            ny = y + dcy[direction]
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] >= 0:
                val += graph[ny][nx]
                if graph[ny][nx] == 0:
                    continue
                for i in range(k-1):
                    nx += dcx[direction]
                    ny += dcy[direction]
                    if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] >= 0:
                        val += graph[ny][nx]
                        if graph[ny][nx] == 0:
                            break
        if val > max_val:
            max_val = val
            destroy_x = x
            destroy_y = y
        elif val == max_val:
            continue
    return destroy_x, destroy_y, max_val


def destroy(start_x, start_y):
    graph[start_y][start_x] = -c-1
    for direction in range(4):
            nx = x + dcx[direction]
            ny = y + dcy[direction]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = -1
                elif graph[ny][nx] == 0:
                    graph[ny][nx] = -c-1
                    continue
                else:
                    graph[ny][nx] = -c-1
                    for i in range(k-1):
                        nx += dcx[direction]
                        ny += dcy[direction]
                        if 0 <= nx < n and 0 <= ny < n:
                            if graph[ny][nx] == -1:
                                graph[ny][nx] = -1
                            elif graph[ny][nx] == 0:
                                graph[ny][nx] = -c-1
                                break
                            else:
                                graph[ny][nx] = -c-1
def heal():
    for i in range(n):
        for j in range(n):
            if graph[i][j] < -2:
                graph[i][j] += 1
            elif graph[i][j] == -2:
                graph[i][j] = 0


input = sys.stdin.readline
n, m, k, c = map(int, input().split())
# n = 격자크기, m = 박멸이 진행되는 년 수, k = 제초제 확산 범위, c = 제초제가 남아있는 년 수#
graph = []
answer = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
dcx, dcy = [1, 1, -1, -1], [1, -1, 1, -1] 

#그래프 초기화
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(m):
    tree_place = []
    seed_axis = []
    
    growth_tree()
    seed()
    namu_plus()
    tree_place.sort(key = lambda x : (x[1], x[0]))
    x, y, destroy_namu = find_destroy()
    #print(x, y)
    #print('before destry')
    #for j in range(n):
    #    print(*graph[j])
    heal()
    if x < 0 and y < 0:
        continue
    destroy(x, y)
    answer += destroy_namu
    #print('after destry')
    #for j in range(n):
    #    print(*graph[j])
print(answer)
