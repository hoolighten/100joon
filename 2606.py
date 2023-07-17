def dfs(graph, v, visit):
    visit[v] = True
    for i in graph[v]:
        if not visit[i]:
            dfs(graph, i, visit)

com_num = int(input())
com_node = int(input())
virus_graph = [[] for _ in range(com_num + 1)]
visited = [False] * (com_num + 1)

for _ in range(com_node):
    start_node, end_node = map(int, input().split())
    virus_graph[start_node].append(end_node)
    virus_graph[end_node].append(start_node)
dfs(virus_graph, 1, visited)
print(visited.count(True) - 1)
