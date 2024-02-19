import sys
input = sys.stdin.readline


def dfs(s):
    visited[s] = True
    s_val = graph[s]
    if not visited[s_val]:
        return dfs(s_val)
    elif visited[s_val]:
        return s_val
    

n = int(input())
graph = [0]*(n+1)
cnt = 0
result = []
for i in range(1, n+1):
    graph[i] = int(input())

for j in range(1, n+1):
    visited = [False]*(n+1)
    if j == dfs(j):
        cnt+=1
        result.append(j)
print(cnt)
for i in result:
    print(i)
