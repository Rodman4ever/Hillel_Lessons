x1 = int(input('enter horizontal Start position: '))
y1 = int(input('enter vertical Start position: '))
x2 = int(input('enter horizontal TARGET position: '))
y2 = int(input('enter vertical TARGET position: '))
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')
