K, N = map(int, input().split())
answer = []

def pick_num(num):
    if (num == N):  # N만큼 뽑았다면 탈출
        print(*answer)
        return
    for i in range(1, K+1):     # K 이하의 수 중 그 다음 수를 append
        answer.append(i)
        pick_num(num + 1)
        answer.pop()
    return
pick_num(0)
