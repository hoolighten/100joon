import sys

k, n = map(int, input().split())
line_list = list()
for i in range(k):
    line_list.append(int(input()))

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for line in line_list:
            cnt += (line // mid)
        if cnt >= target:
            start = mid + 1
        if cnt < target:
            end = mid - 1
    print(end)

binary_search(n, 1, max(line_list))
