def cnt_find(find_graph):
    global n
    cnt_x, cnt_y = 1, 1
    max_x, max_y = -1e8, -1e8
    for j in range(n):
        for i in range(n-1):
            print
            if graph[i][j] == graph[i + 1][j]:
                cnt_x += 1
                max_x = max(cnt_x, max_x)
            else:
                cnt_x = 1
        cnt_x = 1
    for i in range(n):
        for j in range(n-1):
            if graph[i][j] == graph[i][j + 1]:
                cnt_y += 1
                max_y = max(cnt_y, max_y)
            else:
                cnt_y = 1
        cnt_y = 1
    answer = max(max_x, max_y)
    return answer


n = int(input())
graph = [list(input()) for _ in range(n)]
ans = 0
steps = [[-1, 0], [1, 0], [0, 1], [0, -1]]   # 상, 하, 좌, 우

for x in range(n):
    for y in range(n):
        for k in range(4):
            nx = x + steps[k][0]
            ny = y + steps[k][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[x][y] != graph[nx][ny]:
                graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                ans = max(ans, cnt_find(graph))
                graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
print(ans)
