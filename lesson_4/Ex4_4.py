n = int(input('Type number by choice and hit Enter: '))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()
