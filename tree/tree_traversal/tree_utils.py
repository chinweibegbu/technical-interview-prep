from collections import deque

def print_tree(root):
  stack = deque()
  stack.append([root, 0])
  level_str = "\nTree heirarchy:\n"
  prev_level = 0
  level = 0
  while len(stack) > 0:
    prev_level = level
    node, level = stack.pop()
    
    if level > 0 and len(stack) > 0 and level <= stack[-1][1]:
      level_str += "   "*(level-1)+ "├─"
    elif level > 0:
      level_str += "   "*(level-1)+ "└─"
    level_str += str(node.value)
    level_str += "\n"
    level+=1
    for child in node.children:
      stack.append([child, level])
      
  print(level_str)
      
def print_path(path):
  # If path is None, no path was found
  if path == None:
    print("No paths found!")

  # If a path was found, print path
  else:  
    path_string = "{START} "
    for i in range(len(path)-1):
      path_string += path[i].value + " -> "
    path_string += path[-1].value + " {END}"
    print("Path found: {}".format(path_string))