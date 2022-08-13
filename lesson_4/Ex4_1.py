first_day_km = int(input('enter first_day_km: '))
ever_day_km = int(input('enter ever_day_km: '))
days = 1
while first_day_km < ever_day_km:
    first_day_km *= 1.1
    days += 1
print(days)