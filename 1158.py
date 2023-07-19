from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n + 1))
answer = []
while queue:
    for i in range(k - 1):
        move = queue.popleft()
        queue.append(move)
    answer.append(queue.popleft())
print(str(answer).replace('[', '<').replace(']', '>'))


