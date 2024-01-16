import sys

input = sys.stdin.readline

def binary_search(target, data):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return True
        if data[mid] > target:
            end = mid-1
        if data[mid] < target:
            start = mid+1


n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))

for i in range(m):
    answer = binary_search(m_list[i], n_list)
    if answer:
        print(1, end=' ')
    else:
        print(0, end=' ')
