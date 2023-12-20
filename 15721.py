import sys

input = sys.stdin.readline

A = int(input())
T = int(input()) # 구하고자는 몇번째 뻔 or 데기
word = int(input()) # 0이면 뻔 1이면 데기
n = 1
cnt = 0
chair = 0 
bbun_list = []
while T != cnt:
    bbun_list += [0, 1, 0, 1]
    for _ in range(n+1):
        bbun_list.append(0)
    for _ in range(n+1):
        bbun_list.append(1)
    if len(bbun_list) // 2 > T:
        for cnt_num in bbun_list:
  
            if cnt_num == word:
                cnt += 1
                if cnt == T:
                    break
            chair += 1
            if chair > A - 1 :
                chair = 0
    else:
        n += 1
print(chair)
