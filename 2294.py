import sys
input = sys.stdin.readline

n, k = map(int ,input().split())
coin_list = list()
dp = [100001]*(k+1)
dp[0] = 0

for _ in range(n):
    coin_list.append(int(input()))

for i in range(k+1):
    for j in coin_list:
        if i - j >= 0:
            dp[i] = min(dp[i-j]+1, dp[i])
if dp[-1] == 100001:
    print(-1)
else:
    print(dp[-1])
