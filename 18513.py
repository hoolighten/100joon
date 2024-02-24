import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())

points =list(map(int, input().split()))
home_dict = {}

q = deque()
answer = 0
for p in points:
    home_dict[p] = 0
    q.append((p,0))

def bfs():
    global answer
    h_cnt = 0
    while q:
        print(home_dict)
        now, cnt = q.popleft()
        if now-1 not in home_dict:
            q.append((now-1, cnt+1))
            home_dict[now-1] = cnt+1
            answer += cnt+1
            h_cnt += 1
            if h_cnt == k:
                break
        if now+1 not in home_dict:
            q.append((now+1, cnt+1))
            home_dict[now+1] = cnt+1
            answer += cnt+1
            h_cnt += 1
            if h_cnt == k:
                break
    print(answer)
bfs()
