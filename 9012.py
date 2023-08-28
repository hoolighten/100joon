T = int(input())  # Test Case 입력

for i in range(T):
    p_string = input()  # 괄호 string 타입으로 입력
    stack = []  # 괄호의 짝의 여부, -일경우 유효하지 않는 숫자
    for par_s in p_string:
        if par_s == "(":  # 괄호가 (일 경우 append
            stack.append(par_s)
        elif par_s == ")": # 괄호가 )일 경우 stack이 True 일경우 pop을한다. stack이 False일 경우 "NO"를 출력한다.
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else: # for문안에서 break가 실행되지 않을경우 결과를 나타냄
        if not stack: # stack이 비어 있을 경우 Valid ps임
            print("YES")
        else: # stack의 값이 (일 경우를 표현함
            print("NO")