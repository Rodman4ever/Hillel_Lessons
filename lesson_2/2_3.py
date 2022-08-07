v = int(input('Please enter the speed of the cyclist:'))
t = int(input('Please enter the time of the cyclist:'))
m = 100  # довжина маршруту
x = v * t
if v <= 0:
    print(m - - x) # від"ємне значення!

else:
    print(x)
