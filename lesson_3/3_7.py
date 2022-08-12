asked_from_user = input('Please enter an number:')
res = 1
for i in range(1, int(asked_from_user) + 1):
    res *= i
print(str('factorial of ') + str(asked_from_user) + str('  is ') + str(res))

