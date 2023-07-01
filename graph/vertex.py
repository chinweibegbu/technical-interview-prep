class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight = 0):
    print(f"Connecting {vertex} to {self.value}")
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())

  def __eq__(self, other):
    return self.value == other.value

  def __ne__(self, other):
    return self.value != other.value
  
  def __lt__(self, other):
    return ord(self.value[0]) < ord(other.value[0])
  
  def __le__(self, other):
    return ord(self.value[0]) <= ord(other.value[0])
  
  def __gt__(self, other):
    return ord(self.value[0]) > ord(other.value[0])
  
  def __ge__(self, other):
    return ord(self.value[0]) >= ord(other.value[0])
