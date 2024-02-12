import sys

input = sys.stdin.readline
n = int(input())
li_stone = list()
answer = list()
dp = [0]*(n)
for _ in range(n-1):
    li_stone.append(list(map(int, input().split())))
super_jump = int(input())

if n >= 3:
    dp[1] = li_stone[0][0]
    for i in range(2, n):
        dp[i] = min(dp[i-1] + li_stone[i-1][0], dp[i-2] + li_stone[i-2][1])
    answer.append(dp[n-1])
    for i in range(3, n):
        dp[i] = super_jump + dp[i-3]
        if i+1 == n:
            answer.append(dp[-1])
            break
        dp[i+1] = dp[i] + li_stone[i][0]
        for j in range(i+2, n):
            dp[j] = min(dp[j-1] + li_stone[j-1][0], dp[j-2] + li_stone[j-2][1])
    print(min(answer))
elif n == 2:
    answer.append(li_stone[0][0])
    print(min(answer))
else:
    print(0)
