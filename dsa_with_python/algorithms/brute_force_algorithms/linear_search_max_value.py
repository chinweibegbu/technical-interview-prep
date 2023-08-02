# Returns the index of first occurence of the first term
def linear_search_max_value(search_list):
    maximum_value_index = None
    for i in range(len(search_list)):
        if (maximum_value_index == None or my_numbers[i] > my_numbers[maximum_value_index]):
            maximum_value_index = i
    return maximum_value_index

my_numbers = [ 10, 14, 19, 26, 57, 31, 13, 35, 42, 14, 44]

print("Looking for maximum value in {}".format(my_numbers))
max_value_index = linear_search_max_value(my_numbers)
print("Maximum value in list is: {} at index {}".format(my_numbers[max_value_index], max_value_index))
