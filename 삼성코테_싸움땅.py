def dir_transform(d):
    if d == 0:
        return [-1, 0]
    if d == 1:
        return [0, 1]
    if d == 2:
        return [1, 0]
    if d == 3:
        return [0, -1]
def dir_90(d):
    if d == [-1, 0]:
        return [0, 1]
    if d == [0, 1]:
        return [1, 0]
    if d == [1, 0]:
        return [0, -1]
    if d == [0, -1]:
        return [-1, 0]


def move(num):
    _x, _y, _dir = people[num][0][0] + people[num][1][0], people[num][0][1] + people[num][1][1], people[num][1]
    if people[num][0][0] + people[num][1][0] < 0 or people[num][0][0] + people[num][1][0] >= n:
        _x = people[num][0][0] - people[num][1][0]
        _dir = [-people[num][1][0], -people[num][1][1]]
    if people[num][0][1] + people[num][1][1] < 0 or people[num][0][1] + people[num][1][1] >= n:
        _y = people[num][0][1] - people[num][1][1]
        _dir = [-people[num][1][0], -people[num][1][1]]
    return [_x, _y], _dir



def gun_upgrade(num, r, c):
    batch_gun = max(arr[r][c])
    arr[r][c].remove(batch_gun)
    if people[num][3] > batch_gun:          # 현재총이 더 좋을 경우
        return people[num][3], batch_gun   # return 1 : 내가 가질총 2 : 땅에 놔둘 총
    else:
        return batch_gun, people[num][3]


def battle(move_people, stay_people):
    if people[move_people][2] + people[move_people][3] > people[stay_people][2] + people[stay_people][3]:
        score[move_people] += people[move_people][2] + people[move_people][3] - people[stay_people][2] - people[stay_people][3]
        return move_people, stay_people
    if people[move_people][2] + people[move_people][3] < people[stay_people][2] + people[stay_people][3]:
        score[stay_people] += people[stay_people][2] + people[stay_people][3] - people[move_people][2] - people[move_people][3]
        return stay_people, move_people
    if people[move_people][2] + people[move_people][3] == people[stay_people][2] + people[stay_people][3]:
        if people[move_people][2] > people[stay_people][2]:
            score[move_people] += 0
            return move_people, stay_people
        if people[stay_people][2] > people[move_people][2]:
            score[move_people] += 0
            return stay_people, move_people


def loser_move(num):
    #print(people[num])
    flag = 0
    _x = people[num][0][0] + people[num][1][0]
    _y = people[num][0][1] + people[num][1][1]
    for _ in range(3):
        for i in range(m): #사람이 있는지 없는지 여부확인
            if i != num:
                if people[i][0] == [_x, _y]:
                    people[num][1] = dir_90(people[num][1])
                    _x = people[num][0][0] + people[num][1][0]
                    _y = people[num][0][1] + people[num][1][1]
        if _x < 0 or _x >= n or _y < 0 or _y >= n:
            people[num][1] = dir_90(people[num][1])
            _x = people[num][0][0] + people[num][1][0]
            _y = people[num][0][1] + people[num][1][1]
    
    people[num][0] = [_x, _y] # 위치갱신
    return _x, _y


def loser_act(num):
    if people[num][3] > 0:
        arr[people[num][0][0]][people[num][0][1]].append(people[num][3]) #총놔두기
    people[num][3] = 0
    _x, _y = loser_move(num)
    #print(_x, _y)
    big_gun, little_gun = gun_upgrade(num, _x, _y)
    arr[_x][_y].append(little_gun)
    people[num][3] = big_gun


def winner_act(num):
    big_gun, little_gun = gun_upgrade(num, people[num][0][0], people[num][0][1])
    arr[people[num][0][0]][people[num][0][1]].append(little_gun)
    people[num][3] = big_gun

n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    lst = map(int, input().split())
    tmparr = []
    for i in lst:
        tmparr.append([i])
    arr.append(tmparr)
people = dict()
score = [0] * m
for i in range(m):
    x, y, d, s = map(int, input().split())
    people[i] = [[x-1, y-1], dir_transform(d), s, 0]
for i in range(k):
    for player_num in range(m):
        # print('before_move')
        # print(player_num, people[player_num])
        battle_flag = 0
        axis, new_dir = move(player_num)
        people[player_num][0] = axis
        people[player_num][1] = new_dir
        for rival in range(m):
            if player_num != rival:
                if people[rival][0] == people[player_num][0]: #사람을 만났을 경우
                    #print("start battle")
                    battle_flag = 1
                    #print(player_num, people[player_num])
                    winner, loser = battle(player_num, rival) #player_num : 이동한사람, rival : 원래있던사람
                     #print(people[winner], people[loser])
                    loser_act(loser)
                    for i in range(n):
                        for j in range(n):
                            arr[i][j].sort()
                    #print('after lose') 
                    #print('')
                    #print(loser,'after_lose_move', people[loser])
                    winner_act(winner)
                    #print(winner,'after_winner_move',people[winner])

                    break
        if battle_flag == 0: #사람이 없을 경우
            big_gun, little_gun = gun_upgrade(player_num, axis[0], axis[1])
            arr[axis[0]][axis[1]].append(little_gun)
            people[player_num][3] = big_gun
            #for i in range(n):
            #    print(*arr[i])
            # print('after_move')
            # print(player_num, people[player_num])
            # print('')
            # print(player_num,'after upgrade', people[player_num])

        
#     #print('after', people)
print(*score)
