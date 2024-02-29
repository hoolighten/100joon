import sys

n = int(input())

graph = list(map(int, input().split()))
dp = [0]*n
dp[0] = graph[0]

for i in range(1, n):
    graph[i] = max(graph[i] + graph[i-1], graph[i])
print(max(graph))
