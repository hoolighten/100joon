from collections import deque
queue = deque()
# T = int(input())
T = 1
for _ in range(T):
    num_doc, num_index = map(int, input().split())
    queue = deque(map(int, input().split()))
    cnt = 0
    while True:
        num_max = max(queue)
        num_pop = queue.popleft()
        num_index -= 1
        if num_pop < num_max:
            queue.append(num_pop)
            if num_index < 0:
                num_index = len(queue) - 1
        else:
            cnt += 1
            if num_index < 0:
                print(cnt)
                break
