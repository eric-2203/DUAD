def bubble_sort(list_to_sort):
    try: 
        for outer_index in range(0, len(list_to_sort)):
            for index in range(0, len(list_to_sort) -1):
                current_element = list_to_sort[index]
                next_element = list_to_sort[index +1]
                
                #print(f"External iteration: {outer_index}")
                #print(f"Iteration {index}. Current element: {current_element}. Next element: {next_element}.")

                if current_element > next_element:
                    list_to_sort[index] = next_element
                    list_to_sort[index +1] = current_element
    except TypeError:
        print("Format should be a list and it should contain just numbers. If you are using a different format or introducing characters that are not numbers, please correct it.")
        raise

    return list_to_sort
        
    

            


test_list = [3,2,1]

bubble_sort(test_list)

print(test_list)