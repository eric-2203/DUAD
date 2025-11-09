def print_numbers_times_2(numbers_list):
	for number in numbers_list: # O(n)
		print(number * 2)  #  O(1)
		

def check_if_lists_have_an_equal(list_a, list_b):  #Entonces, para esta funcion, el peor de los casos seria O(n*m)?
	for element_a in list_a:   #  O(n)
		for element_b in list_b:   # O(m)
			if element_a == element_b:  # O(1)
				return True    # O(1)
				
	return False  # O(1)


def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):   # O(1)
		print(list_to_print[index])   # O(1)
		

def generate_list_trios(list_a, list_b, list_c):  #La complejidad sería O(a*b*c). Si las 3 listas fuesen del mismo tamaño, seria O(n^3)
	result_list = []
	for element_a in list_a:   # O(a)
		for element_b in list_b:   # O(b)
			for element_c in list_c:   # O(c)
				result_list.append(f'{element_a} {element_b} {element_c}')  # O(1)
				
	return result_list   # O(1)

def is_valid(x):  # La complejidad seria de O(n)
    return x > 10 and x % 3 == 0  # O(1)

def count_valid_elements(numbers):
    count = 0
    for num in numbers:  # O(n)
        if is_valid(num): # O(1)
            count += 1  # O(1)
    return count  # O(1)






