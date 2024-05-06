import sys



def difuse(_r, _c):
    dif_val = int(arr[_r][_c] / 5)
    for drx, dry in zip(dx, dy):
        nx = drx + _r
        ny = dry + _c
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] >= 0:
            difuse_list.append([nx, ny, dif_val])
            arr[_r][_c] -= dif_val


def air_clean(a_list, pid):
    _r = a_list[0]
    _c = a_list[1]
    if pid == 0:
        for up in range(_r - 1, 0, -1):
            arr[up][0] = arr[up-1][0]
        for right in range(c-1):
            arr[0][right] = arr[0][right+1]
        for down in range(_r):
            arr[down][c-1] = arr[down+1][c-1]
        for left in range(c - 1, 1, -1):
            arr[_r][left] = arr[_r][left-1]
    if pid == 1:
        for down in range(_r + 1, r - 1):
            arr[down][0] = arr[down+1][0]
        for right in range(c-1):
            arr[r-1][right] = arr[r-1][right+1]
        for up in range(r - 1, _r -  1, -1):
            arr[up][c-1] = arr[up-1][c-1]
        for left in range(c - 1, 1, -1):
            arr[_r][left] = arr[_r][left-1]
    arr[_r][_c + 1] = 0


r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(r)]
difuse_list = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
air_cleaner = []
answer = 0
for _ in range(t):
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                difuse(i, j)
            elif arr[i][j] < 0:
                air_cleaner.append([i, j])
    for x, y, val in difuse_list:
        arr[x][y] += val
    for num in range(2):
        air_clean(air_cleaner[num], num)
    air_cleaner = []
    difuse_list = []
for i in range(r):
    answer += sum(arr[i])
answer += 2
print(answer)
