import sys
from collections import deque

def bfs(adj_graph, node):
    global visited
    queue = deque([node])
    visited[node] = True
    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')
        for i in adj_graph[current_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True




def dfs(adj_graph, node):
    global visited

    visited[node] = True
    print(node, end=' ')
    for adj_node in adj_graph[node]:
        if not visited[adj_node]:
            dfs(adj_graph, adj_node)

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in graph:
    i.sort()


dfs(graph, v)
visited = [False]*(n+1)
print()
bfs(graph, v)