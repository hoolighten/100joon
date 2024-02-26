import sys

k = int(input())
num = list(map(int,sys.stdin.readline().split()))
length = len(num)
tree = [[] for _ in range(k)]
def get_num(first,last,k):
    if first == last:
        tree[k].append(num[first])
        return
    mid = (first+last) // 2
    tree[k].append(num[mid])
    get_num(first,mid-1,k+1)
    get_num(mid+1,last,k+1) 

get_num(0,length-1,0)

for i in range(k):
    print(*tree[i])
