import sys
from itertools import product
input = sys.stdin.readline

N, K = map(int, input().split())
len_n = len(str(N))
k_list = list(input().split())
temp_max = 0
flag = 1

while flag:
    problem = list(product(k_list, repeat = len_n))
    len_n -= 1
    for i in problem:
        temp = int(''.join(map(str, i)))
        if temp <= N:
            temp_max = max(temp, temp_max)
            flag = 0
print(temp_max)
