from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }


def dijkstras(graph, start):
  distances = {}
  
  # Initialose distances for algorithm
  for vertex in graph:
    distances[vertex] = inf
  distances[start] = 0

  # Create heap for algorithm
  vertices_to_explore = [(0, start)]

  # Continue to run while the heap is not empty
  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    
    # Get the neighbours of the current vertex
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      
      # If the new distance is less than the distance in the distances dictionary...
      if new_distance < distances[neighbor]:
        # Replace distance in dictionary
        distances[neighbor] = new_distance
        # Add the neighbor to the vertices to explore
        heappush(vertices_to_explore, (new_distance, neighbor))

  # Return the distances
  return distances
        
distances_from_d = dijkstras(graph, 'D')
print("\n\nShortest Distances: {0}".format(distances_from_d))
