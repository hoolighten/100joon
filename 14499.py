n_col, m_row, nx, ny, k_order = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n_col)]
order = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else: #남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for i in order:
    nx = nx + dx[i-1]
    ny = ny + dy[i-1]
    if nx < 0 or nx >= n_col or ny < 0 or ny >= m_row:
        nx = nx - dx[i-1]
        ny = ny - dy[i-1]
        continue
    turn(i)
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[-1]
    else:
        dice[-1] = graph[nx][ny]
        graph[nx][ny] = 0
    print(dice[0])