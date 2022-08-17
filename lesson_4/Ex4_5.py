user_list = []
for i in range(3, 159, 2):
    user_list.append(i)
print("All  element of list is:", user_list)
print("Third  element of list is:", user_list[2])
print("Penultimate element of list is:", user_list[-2])
print("First 5 elements of list is:", user_list[:5])
print("Elements with even index is:", user_list[::2])
print("Elements with odd index is:", user_list[1::2])
print("Reversed list is:", list(reversed(range(3, 159, 2))))
print("Reversed list with odd index elements is:", list(reversed(range(3, 159, 2)[1::2])))
print("List length is:", len(user_list))



