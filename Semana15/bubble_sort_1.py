def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort)):
        for index in range(0, len(list_to_sort) -1):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index +1]
            
            print(f"External iteration: {outer_index}")
            print(f"Iteration {index}. Current element: {current_element}. Next element: {next_element}.")

            if current_element > next_element:
                list_to_sort[index] = next_element
                list_to_sort[index +1] = current_element


test_list = [10, 8, 5, 4, 3]

bubble_sort(test_list)

print(test_list)