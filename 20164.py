import sys
import math

max_val = 0
min_val = 1e9

def odd(num_str, res):
    global min_val, max_val
    for le in num_str:
        if int(le) % 2 == 1:
            res += 1
    if len(num_str) == 1:
        min_val = min(res, min_val)
        max_val = max(res, max_val)
        return
    if len(num_str) == 2:
        odd(str(int(num_str[0]) + int(num_str[1])), res)
    else:
        for i in range(1, len(num_str) - 1):
            for j in range(i + 1, len(num_str)):
                odd(str(int(num_str[0:i]) + int(num_str[i:j]) + int(num_str[j:])), res)

odd(sys.stdin.readline().rstrip(), 0)
print(min_val, max_val)
