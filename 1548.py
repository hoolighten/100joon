import sys

input = sys.stdin.readline

n = int(input())
tri_li = list(map(int, input().split()))
tri_li.sort()
answer = 0
if n < 3:
    print(n)
else:
    answer = 2
    for i in range(n-2):
        min_val = tri_li[i]
        next_min_val = tri_li[i+1]
        for j in range(n-1, i+1, -1):
            max_val = tri_li[j]
            if min_val + next_min_val > max_val:
                answer = max(j - i + 1, answer)
                break
    print(answer)
