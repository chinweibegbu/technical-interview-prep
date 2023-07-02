import random
from random import randrange
from graph import Graph
from vertex import Vertex

def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      cv = graph.graph_dict[vertex]
      print("=> " + adjacent_vertex + " (weight:" + str(cv.get_weight(adjacent_vertex)) + ")")

def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g

# Define your functions below:
def all_visited(vertex_statuses):
  for vertex_status in vertex_statuses:
    if vertex_statuses[vertex_status] == "unvisited":
      return False
  return True

def traveling_salesperson(graph):
  path = ""
  vertex_statuses = {}
  for vertex in graph.graph_dict.keys():
    vertex_statuses[vertex] = "unvisited"
  current_vertex = random.choice(list(graph.graph_dict))
  print("\nStarting vertex: " + current_vertex)
  vertex_statuses[current_vertex] = "visited"
  path += current_vertex
  visited_all_vertices = all_visited(vertex_statuses)
  while not visited_all_vertices:
    current_vertex_edges = graph.graph_dict[current_vertex].get_edges()
    current_vertex_edge_weights = {}
    for edge in current_vertex_edges:
      current_vertex_edge_weights[edge] = graph.graph_dict[current_vertex].get_weight(edge)
    found_next_vertex = False
    next_vertex = ""
    while not found_next_vertex:
      if len(current_vertex_edge_weights) == 0:
        break
      next_vertex = min(current_vertex_edge_weights, key=current_vertex_edge_weights.get)
      if vertex_statuses[next_vertex] == "unvisited":
        found_next_vertex = True
      elif vertex_statuses[next_vertex] == "visited":
        current_vertex_edge_weights.pop(next_vertex)
    if current_vertex_edge_weights is None:
      visited_all_vertices = True
    else:
      current_vertex = next_vertex
      vertex_statuses[current_vertex] = "visited"
      path += current_vertex
      visited_all_vertices = all_visited(vertex_statuses)
  print("Shortest path: " + path)

travel_graph = build_tsp_graph(False)
print_graph(travel_graph)
traveling_salesperson(travel_graph)
