a = [10, 15, 23, -69, 19, 7, 235, 6, 3, 77]
b = [11, 22, 23, -32, 19, 8, 69, 5, 3, 77]

c = []
d = []
e = a + b

for i in a:
    for j in b:
        if i == j:
            c.append(i)
            break

print(c)

for i in a:
    for j in b:
        if i != j:
            d.append(i)
            break
print(d)

unique_numbers = list(set(e))
print(unique_numbers)


