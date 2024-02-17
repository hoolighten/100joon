import sys

input = sys.stdin.readline
h,w = map(int, input().split())
rainy_list = list(map(int, input().split()))
cnt = 0
for i in range(1, w-1):
    left_max = max(rainy_list[:i])
    right_max = max(rainy_list[i+1:])
    val = min(left_max, right_max) - rainy_list[i]
    if val > 0:
        cnt += val
print(cnt)
