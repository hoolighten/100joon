import sys
import math
import time

def tree_cutting(t_list, height):
    tree_sum = 0
    for tree_height in t_list:
        if height < tree_height:
            tree_sum += (tree_height - height)
    return tree_sum     

n, m = map(int,input().split())
tree_list = list(map(int, input().split()))
start, end = 1, max(tree_list)

while start <= end:
    mid = (start + end) // 2
    ans = tree_cutting(tree_list, mid)
    if ans < m:
        end = mid - 1
    else:
        start = mid + 1
print(end)
