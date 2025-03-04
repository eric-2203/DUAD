my_list = [4, 3, 2, 5, 6, 7]
my_list_2 = []
for num in my_list: 
    if num == my_list[0]:
        my_list_2.append(my_list[-1])
    elif num == my_list[-1]:
        my_list_2.append(my_list[0])
    else:
        my_list_2.append(num)
print(my_list_2)
