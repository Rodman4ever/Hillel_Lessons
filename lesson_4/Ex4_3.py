a, b = [int(input('Type two numbers by choice and hit Enter: ')) for i in range(2)]
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)
