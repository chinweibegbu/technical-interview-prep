from collections import deque
from bfs_tree_node import TreeNode
from tree_utils import print_tree, print_path

# Breadth-first search function
def bfs(root_node, goal_value):

  # initialize frontier queue
  path_queue = deque()

  # add root path to the frontier
  initial_path = [root_node]
  path_queue.appendleft(initial_path)
  
  # search loop that continues as long as
  # there are paths in the frontier
  while path_queue:
    # get the next path and node 
    # then output node value
    current_path = path_queue.pop()
    current_node = current_path[-1]
    print(f"Searching node with value: {current_node.value}")

    # check if the goal node is found
    if current_node.value == goal_value:
      return current_path

    # add paths to children to the  frontier
    for child in current_node.children:
      new_path = current_path.copy()
      new_path.append(child)
      path_queue.appendleft(new_path)

  # return an empty path if goal not found
  return None

# Construct tree
sample_root_node = TreeNode("This PC")
two = TreeNode("Photos")
three = TreeNode("Downloads")
four = TreeNode("stray-kids.png")
five = TreeNode("screenshot-201221-1458.jpg")
six = TreeNode("vlc-3.0.18-win64.exe")
seven = TreeNode("arduino-ide_2.0....4_Windows_64bit.exe")
sample_root_node.children = [three, two]
two.children = [five, four]
three.children = [seven, six]

# Print constructed tree
print_tree(sample_root_node)

# Call DFS on the contructed tree
found_path = bfs(sample_root_node, "stray-kids.png")
print_path(found_path)
