my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
pair_numbers = []
for num in my_list: 
    if num % 2 == 0:
        pair_numbers.append(num)
print(pair_numbers)