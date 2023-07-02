# Class author: Codecademy @ 2023
class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Class author: Codecademy @ 2023
class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
  
  def insert(self, new_node):
    current_node = self.head_node

    if not current_node:
      self.head_node = new_node

    while(current_node):
      next_node = current_node.get_next_node()
      if not next_node:
        current_node.set_next_node(new_node)
      current_node = next_node

  def __iter__(self):
    current_node = self.head_node
    while(current_node):
      yield current_node.get_value()
      current_node = current_node.get_next_node()

  # Function author: Chinwe @ 2023
  def display(self):
    output = "HEAD >>>>   "
    current = self.head_node
    while current.get_next_node() is not None:
        output += " {} -> ".format(current.get_value())
        current = current.get_next_node()
    output += " {} ".format(current.get_value())
    output += "  >>>> TAIL"
    print(output)
