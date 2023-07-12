k = int(input())
money_list = []

for i in range(k):
    money = int(input())
    if money == 0:
        money_list.pop()
    else:
        money_list.append(money)
print(sum(money_list))

