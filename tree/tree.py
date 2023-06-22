class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.children = [] # references to other nodes

  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.value)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

grandmother = TreeNode("Natasha Zhudro")
mother = TreeNode("Gloria Umoren")
aunt = TreeNode("Emem Umoren")
uncle = TreeNode("Victor Umoren")
me = TreeNode("Chinwe Ibegbu")
sister_1 = TreeNode("Daby Ibegbu")
sister_2 = TreeNode("Didi Ibegbu")

grandmother.add_child(mother)
grandmother.add_child(aunt)
grandmother.add_child(uncle)
mother.add_child(me)
mother.add_child(sister_1)
mother.add_child(sister_2)

grandmother.traverse()
