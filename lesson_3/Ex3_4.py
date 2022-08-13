list_of_six = range(100, 197, 6)
for item in list_of_six:
    if item % 5 == 0 and item < 150:
        print(item)