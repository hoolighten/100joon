import sys
import copy


def red_hei():
    max_val = -1
    for x, y in blk[num]:
        max_val = max(red_height[x+r], max_val)
    return max_val


def yel_hei():
    max_val = -1
    for x, y in blk[num]:
        max_val = max(yel_height[y+c], max_val)
    return max_val


def red_tetris(d):
    _red_arr = copy.deepcopy(red_arr)
    for i in range(d):
        for j in range(6):
            red_arr[j][i+1] = _red_arr[j][i]
      
            
def yel_tetris(d):
    _yel_arr = copy.deepcopy(yel_arr)
    for j in range(d):
        for i in range(6):
            yel_arr[j+1][i] = _yel_arr[j][i]


k = int(input())
blk = {1:[[0, 0]], 2:[[0, 0], [0, 1]], 3:[[0, 0], [1, 0]]}
red_height = [0, 0, 0, 0]
red_arr = [[0]*6 for i in range(6)]
yel_height = [0, 0, 0, 0]
yel_arr = [[0]*6 for i in range(6)]
ans = 0
score = 0
over = list()


for i in range(k):
    num, r, c = map(int, input().split())
    r_h = red_hei() # 현재 r값에 위치한 높이
    y_h = yel_hei()
    for plus_r, plus_c in blk[num]:
        new_c = c + plus_c 
        new_r = r + plus_r
        # red 무브
        if new_r == r:
            r_h += 1
            red_height[r] = r_h
        else:
            red_height[new_r] = r_h
        red_arr[new_r][6 - r_h] = 1
        # yello 무브
        if new_c == c:
            y_h += 1
            yel_height[c] = y_h
        else:
            yel_height[new_c] = y_h
        yel_arr[6 - y_h][new_c] = 1
    #print('move graph',num, r, c)
    #for i in range(6):
    #   print(*red_arr[i],' ', *yel_arr[i])
    #print('\n')
       
    for i in range(6):
        chk = 0
        for j in range(4):
            if red_arr[j][i] == 1:
                chk += 1
        if chk == 4:
            #print('red_tetrio')
            over.append(i)
            
    for i in range(len(over)):
        score +=1
        red_tetris(over[i])
        for k in range(4):
            if red_height[k] < 1:
                red_height[k] = 0
            else:
                red_height[k] -= 1
                red_arr[k][0] = 0
        for ov in range(2, 6):
            if red_arr[new_r][ov] == 1:
                red_height[new_r] = 6-ov
            else:
                red_height[new_r] = 0
    #print("r-h",red_height)
    over.clear()
    
    # 옐로 테트리스일 경우 맨아래부터 확인
    for j in range(6):
        chk = 0
        for i in range(4):
            if yel_arr[j][i] == 1:
                chk += 1
        if chk == 4:
            #print('yel_tetrio')
            over.append(j)
            
    for i in range(len(over)):
        score +=1
        yel_tetris(over[i])
        for k in range(4):
            if yel_height[k] < 1:
                yel_height[k] = 0
            else:
                yel_height[k] -= 1
                yel_arr[0][k] = 0
        #print("y-h",yel_height)
        #print(over[i])
        for ov in range(2,6):
            if yel_arr[ov][new_c] == 1:
                yel_height[new_c] = 6-ov
            else:
                yel_height[new_c] = 0
    #print("y-h",yel_height)
    over.clear()
    
    
    # over 해서 밑에줄 없애 
    for i in range(6):
        for j in range(4):
            if red_arr[j][i] == 1 and i < 2:
                #print('red break tetris')
                red_tetris(5)
                for k in range(4):
                    if red_height[k] < 1:
                        red_height[k] = 0
                    else:
                        red_height[k] -= 1
                        red_arr[k][0] = 0
    for j in range(6):
        for i in range(4):
            if yel_arr[j][i] == 1 and j < 2:
                #print('yello break tetris')
                yel_tetris(5)
                for k in range(4):
                    if yel_height[k] < 1:
                        yel_height[k] = 0
                    else:
                        yel_height[k] -= 1
                        yel_arr[0][k] = 0

    # 레드 테트리스일 경우 맨아래부터 확인

    #print('after_tetris_graph')
    #for i in range(6):
    #    print(*red_arr[i],' ', *yel_arr[i])
    #print('레드의 높이',red_height)
    #print('옐로의 높이',yel_height)
for i in range(6):
    for j in range(6):
        if red_arr[i][j] == 1:
            ans +=1
        if yel_arr[i][j] == 1:
            ans +=1
print(score)
print(ans)
