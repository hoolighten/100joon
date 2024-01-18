import sys

input = sys.stdin.readline
str_n = input().split('-')
ans = list()

for exp in str_n:
    plus = 0
    num_list = exp.split('+')
    for num in num_list:
        plus += int(num)
    ans.append(plus)
start = ans[0]

for i in range(1, len(ans)):
    start -= ans[i]
print(start) 
