import sys

input_function = sys.stdin.readline
word = input_function().rstrip() + ' '
answer = list()
num_idx = 0
flag = False

for idx in range(len(word)):
    if not flag:
        if word[idx] == ' ':
            answer.append(word[num_idx:idx][::-1]+' ')
            num_idx = idx+1
        if word[idx] == '<' and not answer:
            answer.append(word[num_idx:idx])
            num_idx = idx
            flag = True
        if word[idx] == '<' and answer:
            answer.append(word[num_idx:idx][::-1])
            num_idx = idx
            flag = True
    else:
        if word[idx] == '>':
            answer.append('<'+word[num_idx+1:idx]+'>')
            flag = False
            num_idx = idx + 1

print(''.join(answer))
