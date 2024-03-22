from collections import deque
import sys
input = sys.stdin.readline 
n = list(input().rstrip())
result = ['']*(len(n)+1)

def dfs(start, arr):
    if not arr:
        return 0
    min_val = min(arr)
    temp = arr.index(min_val)
    result[start + temp] = min_val
    print(''.join(result))
    dfs(start+temp+1,arr[temp+1:])
    dfs(start,arr[:temp])

dfs(1, n)    

# for i in range(len(n)):
#     find_val = sorted(n[i:len(n)])[0]
#     n.remove(find_val)
#     print(n)
