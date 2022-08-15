# _enter_numbers_ = list(map(int(input('please enter numbers :').split( ))))
# _counter_ = 0
# _sum_ = 0
# while _enter_numbers_ != 0:
#   _enter_numbers_ = int(input('please enter numbers :'))
# print(_enter_numbers_)
# _counter_ += 1
# _sum_ = sum(_enter_numbers_)
# print(str('amount of numbers is :  ') + str(_counter_))
# _sum_ = int(_enter_numbers_)
# print(str('sum of numbers is :  ') + str(_sum_))

user_list = []
import.functools
print("PRESS 0 to see: \n\t 1. Amount of numbers \n\t 2. Sum \n\t 3. Average \n\t 4. Minimum \n\t 5. Maximum \n\t 4. Maximum ")

while True:
    value = int(input('Type number by choice and hit Enter: '))
    if value != 0:
        user_list.append(value)
    else:
        break
count_of = len(user_list)
sum_of = sum(user_list)
max_of = max(user_list)
min_of = min(user_list)
avg_of = sum_of / len(user_list)
mult_of = reduce(user_list)
print(count_of)
print(sum_of)
print(max_of)
print(min_of)
print(avg_of)
