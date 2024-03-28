import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
result = list(input().rstrip())
ladder = list(input().rstrip() for _ in range(n))
u_ladder = list()
d_ladder = list()
start = sorted(result)
answer = list()
for i in range(n):
    if ladder[i][0] == '?':
        u_ladder = ladder[:i]
        d_ladder = ladder[i+1:]
        break
for i in range(len(u_ladder)):
    for j in range(k-1):
        if u_ladder[i][j] == '-':
            start[j], start[j+1] = start[j+1], start[j]
for i in range(len(d_ladder)-1, -1, -1):
    for j in range(k-1):
        if d_ladder[i][j] == '-':
            result[j], result[j+1] = result[j+1], result[j]

for i in range(k-1):
    if start[i] == result[i]:
        answer.append('*')
    else:
        start[i], start[i+1] = start[i+1], start[i]
        answer.append('-')
if start == result:
    print(''.join(answer))
else:
    print('x'*(k-1))
