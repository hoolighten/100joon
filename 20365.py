import sys

n = int(input())
painting = input()
r, b = 0, 0
if painting[0] == 'B':
    b += 1
if painting[0] == 'R':
    r += 1
idx = 1
while idx != n:
    if painting[idx] == painting[idx-1]:
        idx +=1
        continue
    else:
        if painting[idx] == 'R':
            r += 1
        elif painting[idx] == 'B':
            b += 1
        idx += 1
print(min(r, b) + 1)
