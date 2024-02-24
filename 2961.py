import sys
import itertools
input = sys.stdin.readline
n = int(input())

SB_list = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9
for i in range(1, n + 1):

    nCr = list(itertools.combinations(SB_list,i))
    for a in nCr:
        sour_taste = 1
        bitter_taste = 0
        for b in a:
            sour_taste *= b[0]
            bitter_taste += b[1]
        answer = min(abs(sour_taste-bitter_taste), answer)
print(answer)
