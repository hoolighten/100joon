dp = [0]*500000

def lay_Find(n):
    if n == 1 or n == 0:
        return 1
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = n - 1 + lay_Find(n - 1)
        return dp[n]


user_input = int(input())

for lay in range(1, 100000):
    if lay_Find(lay) <= user_input < lay_Find(lay + 1):
        break
top = user_input-lay_Find(lay) + 1
bottom = lay - top + 1
if lay % 2 == 0:
    print(f'{top}/{bottom}')
elif lay % 2 == 1:
    print(f'{bottom}/{top}')
