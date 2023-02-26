import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def DFS(node, cnt):
    visited[node] = 1

    for adj_node in graph[node]:
        if visited[adj_node] == 0:
            cnt = DFS(adj_node, cnt + 1)

    return cnt


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)

    for _ in range(M):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    print(DFS(1, 0))
