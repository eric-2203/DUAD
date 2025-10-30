def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort)): # O(n)
        changes_made = False
        for index in range(0, len(list_to_sort) -1 - outer_index): #O(n^2)
            current_element = list_to_sort[index]
            next_element = list_to_sort[index +1]
            
            print(f"External iteration: {outer_index}")   # O(1)
            print(f"Iteration {index}. Current element: {current_element}. Next element: {next_element}.")  # O(1)

            if current_element > next_element:  # O(1)
                list_to_sort[index] = next_element
                list_to_sort[index +1] = current_element
                changes_made = True

        if not changes_made: # O(1)
            return  # O(1)
test_list = [3, 4, 5, 6, 8, 7]   # O(1)"

bubble_sort(test_list)  # O(1)

print(test_list)   # O(1)