from dfs_tree_node import TreeNode
from tree_utils import print_tree, print_path

#  Returns the path to the target if its exists
def dfs(root, target, path=()):
  path = path + (root,)

  # If the root is the target, return the current path
  if root.value == target:
    return path
  
  # For each child of the root, recursively call DFS
  for child in root.children:
    path_found = dfs(child, target, path)

    # If a path is found (i.e. the target is found), return the current path
    if path_found is not None:
      return path_found
  
  # If a path is not found (i.e. the target is not found), return None
  return None

# Construct tree
sample_root_node = TreeNode("A")
two = TreeNode("B")
three = TreeNode("C")
four = TreeNode("D")
five = TreeNode("E")
six = TreeNode("F")
seven = TreeNode("G")
sample_root_node.children = [three, two]
two.children = [five, four]
three.children = [seven, six]

# Print constructed tree
print_tree(sample_root_node)

# Call DFS on the contructed tree
found_path = dfs(sample_root_node, "F")
print_path(found_path)
