import sys
import math
input = sys.stdin.readline

n = int(input())
increase_list = list(map(int, input().split()))
val = -1
dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if increase_list[i] > increase_list[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
