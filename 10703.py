import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = [input() for _ in range(n)]
def get_dist():
    dist = n
    for j in range(m):
        meteor = -3001 
        for i in range(n):
            if arr[i][j] == "X": 
                meteor = i
            elif arr[i][j] == "#":
                dist = min(i - meteor - 1,dist)
                break
    return dist

dist = get_dist()

for i in range(dist):
    res = ""
    for j in range(m):
        if arr[i][j] == "#":
            res += "#"
        else:
            res += "."
    print(res)
for i in range(dist, n):
    res = ""
    for j in range(m):
        if arr[i-dist][j] == "X":
            res += "X"
        elif arr[i][j] == "#":
            res += "#"
        else:
            res += "."
    print(res)
