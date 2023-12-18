import sys
import time

start = time.time()
M, N = map(int, input().split())
board = list()
cnt = list()


for _ in range(M):
    row = sys.stdin.readline().rstrip()
    board.append(row)
    
for start_M in range(M-7):
    for start_N in range(N-7):
        w_count = 0
        b_count = 0
        for i in range(start_M, start_M+8):
            for j in range(start_N, start_N+8):
                if (i+j)%2 == 0:
                    if board[i][j] == 'W':
                        b_count +=1 ## 시작이 B
                    else:
                        w_count +=1 ## 시작이 W
                else:
                    if board[i][j] == 'W':
                        w_count += 1 ## 시작이 B
                    else:
                        b_count += 1 ## 시작이 W
        cnt.append(w_count)
        cnt.append(b_count)
print(min(cnt))
