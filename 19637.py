import sys
import math

def binary(p):
    start = 0
    end = len(power_list) -1

    while start <= end:
        mid = (start + end) // 2
        if p > power_list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    print(word_list[end+1])

input = sys.stdin.readline

n, m = map(int, input().split())
word_list = []
power_list = []
for _ in range(n):
    word, power = map(str, input().split())
    power = int(power)
    if power_list and power_list[-1] == power:
        continue
    power_list.append(power)
    word_list.append(word)

for i in range(m):
    p = int(input())
    binary(p)
