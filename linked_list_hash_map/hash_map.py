from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]
  
  def hash(self, key):
    key_bytes = key.encode()
    return sum(key_bytes)
  
  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    payload = Node([key, value])
    current = list_at_index.head_node

    # If linkedlist is empty, insert payload
    if current is None:
      list_at_index.insert(payload)
      return
    
    # If linkedlist is not empty
    while current != None:
      # Get the pair of the current node
      current_pair = current.get_value()

      # If the pair has the same key, overwrite
      if current_pair[0] == key:
        current.set_value(payload)
        return
      current = current.get_next_node()
    
    # Add node to end of linkedlist
    list_at_index.insert(payload)
    return

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    current = list_at_index.head_node

    # If linkedlist is empty, insert payload
    if current is None:
      return None
    
    # If linkedlist is not empty
    while current != None:
      # Get the pair of the current node
      current_pair = current.get_value()

      # If the pair has the same key, overwrite
      if current_pair[0] == key:
        return current_pair[1]
      if current_pair[0] != key:
        current = current.get_next_node()
  
blossom = HashMap(len(flower_definitions))
for item in flower_definitions:
  blossom.assign(item[0], item[1])
print(blossom.retrieve("daisy"))
print(blossom.retrieve("rose"))
