T = int(input())

for i in range(T):
    floor = int(input())
    ho = int(input())
    map = [i for i in range(1, ho+1)]
    for k in range(floor):
        for j in range(1, ho):
            map[j] += map[j-1]
    print(map[ho-1])