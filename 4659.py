import sys
input = sys.stdin.readline

def word_check_1(_word):
    for i in moum:
        if i in _word:
            return word_check_2(_word)
    # print(_word, 'not moum')
    return False

def word_check_2(_word):
    m_cnt = 0
    j_cnt = 0
    if _word[0] in moum:
        m_cnt = 1
    else:
        j_cnt = 1
    for i in range(1, len(_word)):
        if _word[i] == _word[i-1]:
            if _word[i] == 'e' or _word[i] == 'o':
                pass
            else:
                # print(_word, 'continued not ee or oo')
                return False
        if _word[i] in moum:
            m_cnt += 1
            j_cnt = 0
        else:
            j_cnt += 1
            m_cnt = 0
        if m_cnt > 2 or j_cnt > 2:
            # print(_word, 'continued m or j')
            return False
    return True

        


moum = ['a', 'e', 'i', 'o', 'u']


while True:
    word = input().rstrip()
    if word == 'end':
        break
    else:
        if word_check_1(word) == True:
            print('<%s> is acceptable.' %word)
        else:
            print('<%s> is not acceptable.' %word)
