import time
start = time.time()
n = int(input())

cnt = 0

while True:
    if n % 5 == 0:
        cnt += n//5
        print(cnt)
        break
    else:
        n -= 2
        if n == -2:
            print(cnt)
            break
        cnt += 1
    if n < 0:
        print(n)
        break


