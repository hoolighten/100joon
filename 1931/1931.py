n = int(input())
room = []
cnt = 1
for i in range(n):
    start_time, end_time = map(int, input().split())
    room.append([start_time, end_time])
room.sort(key = lambda x: x[0])
room.sort(key = lambda x: x[1])

end = room[0][1]

for i in range(1, n):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]
print(cnt)