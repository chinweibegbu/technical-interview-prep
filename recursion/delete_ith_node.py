from delete_ith_node_helper import Node, LinkedList

# define remove_node() here
# Function author: Codecademy
def remove_node(head, i):
  # Edge case: i is negative
  if i < 0:
    return head
  
  # Base cases
  if head is None:
    return None
  if i == 0:
    return head.next_node

  head.next_node = remove_node(head.next_node, i - 1)
  return head

# Test code
items = ["Amber", "Sapphire", "Jade", "Pearl"]
gemstones = LinkedList()
for item in items:
  gemstones.insert(Node(item))

head = remove_node(gemstones.head_node, 2)
if head is not None:
  gemstones.display()
else:
  print("This is an empty list!")
