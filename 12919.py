import sys
input = sys.stdin.readline

def dfs(val):
    if val==S:
        print(1)
        exit()
    if len(val) == 0:
        return 0
    if val[0] == 'B':
        dfs(val[1:][::-1])
    if val[-1] == 'A':
        dfs(val[:-1])
    
    
    
S = list(input().rstrip())
T = list(input().rstrip())

dfs(T)
print(0)
