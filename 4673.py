def self_num(number, sum_num):
    digit = number % 10
    if number == 0:
        return sum_num
    else:
        sum_num += digit
        number //= 10
        return self_num(number, sum_num)


num = []
for i in list(range(1, 10001)):
    num.append(self_num(i, 0) + i)
    if i not in num:
        print(i)

