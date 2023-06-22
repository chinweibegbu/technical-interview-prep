# Returns the index of first occurence of the first term
def linear_search_all_occurences(search_list, target_value):
    matches = []
    for i in range(len(search_list)):
        if search_list[i] == target_value:
            matches.append(i)
    if matches:
       return matches
    # If target_value is not in list, raise a ValueError exception
    raise ValueError("{} is not in list".format(target_value))

my_numbers = [ 10, 14, 19, 26, 57, 31, 13, 35, 42, 14, 44]
search_term_1, search_term_2 = 23, 14

try:
    print("Looking for {} in {}".format(search_term_1, my_numbers))
    matches_1 = linear_search_all_occurences(my_numbers, search_term_1)
    print("{} is in list at indeces {}".format(search_term_1, matches_1))
except ValueError as error_message:
  print("{0}".format(error_message))

try:
    print("\nLooking for {} in {}".format(search_term_2, my_numbers))
    matches_2 = linear_search_all_occurences(my_numbers, search_term_2)
    print("{} is in list at indeces {}".format(search_term_2, matches_2))
except ValueError as error_message:
  print("{0}".format(error_message))
