k = int(input())
dir_dist_map = [[] for i in range(2)]
blank_dist = []
all_size = []
for i in range(6):
    _dir, _dist = map(int, input().split())
    if _dir < 3:
        dir_dist_map[0].append(_dist)
    else:
        dir_dist_map[1].append(_dist)

for j in dir_dist_map:
    all_size.append(max(j))
    if max(j) == j[0]:
        blank_dist.append(j[2])
    else:
        blank_dist.append(j[1])
answer = ((all_size[0]*all_size[1])-(blank_dist[0]*blank_dist[1])) * k
