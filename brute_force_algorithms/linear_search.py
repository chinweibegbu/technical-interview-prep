# Returns the index of first occurence of the first term
def linear_search(search_list, target_value):
    for i in range(len(search_list)):
        if search_list[i] == target_value:
            return i
    # If target_value is not in list, raise a ValueError exception
    raise ValueError("{} is not in list".format(target_value))

my_numbers = [ 10, 14, 19, 26, 57, 31, 13, 35, 42, 14, 44]
search_term_1, search_term_2 = 23, 14

try:
    print("Looking for {} in {}".format(search_term_1, my_numbers))
    idx_1 = linear_search(my_numbers, search_term_1)
    print("{} is in list at index {}".format(search_term_1, idx_1))
except ValueError as error_message:
  print("{0}".format(error_message))

try:
    print("\nLooking for {} in {}".format(search_term_2, my_numbers))
    idx_2 = linear_search(my_numbers, search_term_2)
    print("{} is in list at index {}".format(search_term_2, idx_2))
except ValueError as error_message:
  print("{0}".format(error_message))
