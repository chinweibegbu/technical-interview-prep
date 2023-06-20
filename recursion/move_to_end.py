# define move_to_end() here
def move_to_end(my_list, my_string):
  # Re-ordered list
  result = []

  # Base case
  if len(my_list) == 0:
    return []

  # Recursive step
  # (a) If you have found the search term, add it after the rest
  if my_list[0] == my_string:
    result += move_to_end(my_list[1:], my_string)
    result.append(my_list[0])
  # (b) If you have not found the search term, add it like a normal element to the resulting list
  else:
    result.append(my_list[0])
    result += move_to_end(my_list[1:], my_string)
  
  return result

# Test code - do not edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))
