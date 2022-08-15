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
import numpy

while True:
    value = int(input('Type number by choice and hit Enter: '))
    if value != 0:
        user_list.append(value)
    else:
        break
count_of = len(user_list)
sum_of = sum(user_list)
mult_of = numpy.prod(user_list)
avg_of = sum_of / len(user_list)
max_of = max(user_list)
enum_of = user_list.index(max(user_list)) + 1
odd_count = len(list(filter(lambda x: (x % 2 != 0), user_list)))
even_count = len(list(filter(lambda x: (x % 2 == 0), user_list)))
quan_max = len(list(filter(lambda x: (x == max_of), user_list)))

print("Quantity of elements is:", count_of)
print("Sum of elements is:", sum_of)
print("Multiply of elements is:", mult_of)
print("Average of elements is:", avg_of)
print("Max of elements is:", max_of)
print("index of max element is:", enum_of)
print("Quantity of odd (нечет) element is:", odd_count)
print("Quantity of even (чет) element is:", even_count)
print("Second largest element is:", sorted(user_list)[-2])
print("Quantity of max element is:", quan_max)

