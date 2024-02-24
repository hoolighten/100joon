import sys

input = sys.stdin.readline
n, m = map(int, input().split())
cnt = 0
listen_li = set()
for _ in range(n):
    listen_li.add(input().rstrip())
see_li = set()
for _ in range(m):
    see_li.add(input().rstrip())
answer = sorted(see_li & listen_li)
print(len(answer))
for ans in answer:
    print(ans)
