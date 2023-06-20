def find_min(my_list):
  # Edge case: Input is not a list
  if not isinstance(my_list, list):
    return Exception("Input is of wrong type")

  # Edge case: List is empty
  if len(my_list) == 0:
    return None
  
  # Base case
  if len(my_list) == 1:
    return my_list[0]
  # Recursive step
  first_element = my_list[0]
  sub_list_min = find_min(my_list[1:])
  return (first_element if first_element <= sub_list_min else sub_list_min)
  # alternative return statement:
  # return min(first_element, sub_list_min)


# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)
