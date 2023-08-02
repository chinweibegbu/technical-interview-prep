def tree_depth(tree):
  # Edge case: Empty list
  if len(tree) == 0:
    return 0
  
  # Base case
  if tree["left_child"] is None:
    return 1
  # Recursive step
  return tree_depth(tree["left_child"]) + 1  

# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node

# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 

# test cases
print(tree_depth(tree_level_1) == 1)
print(tree_depth(tree_level_2) == 2)
print(tree_depth(tree_level_4) == 4)