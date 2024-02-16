import sys
input = sys.stdin.readline

n, k = map(int ,input().split())
coin_list = list()
dp = [0]*(k+1)
dp[0] = 1

for _ in range(n):
    coin_list.append(int(input()))

for i in coin_list:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
print(dp[-1])
