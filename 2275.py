T = int(input())

for i in range(T):
    floor = int(input())
    ho = int(input())
    map = [i for i in range(0, ho+1)]
    if floor == 0:
        print(map[-1])
    else:
        for _ in range(floor):
            for j in range(1, ho+1):
                map[j] = map[j] + map[j-1]
        print(map[-1])
