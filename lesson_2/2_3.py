v = int(input('Please enter the speed of the cyclist:'))
t = int(input('Please enter the time of the cyclist:'))
x = v * t
if v <= 0:
    print(0)
# відємне значення швидкості згідно з завданням допустиме, проте вірною відповіддю мав в даному випадку бути 0
else:
    print(v * t)  # отримуємо число а не стрічку
