import sys

n, k = map(int, input().split())
ans_list = list()
for i in range(1, int(n**(1/2))+1):
    if n % i == 0:
        ans_list.append(i)
        if n // i != i:
            ans_list.append(n//i)
ans_list.sort()
if k-1 >= len(ans_list):
    print(0)
else:
    print(ans_list[k-1])
