from graph import Graph
from vertex import Vertex
from collections import deque
from script import print_graph

# DFS Post-order Traversal function
# Function author: Chinwe @ 2023
def dfs_post_order(graph, start_vertex):
    # Get vertices from graph
    vertices = graph.graph_dict

    # Create list to track visited vertices and stack for traversal
    visited = []
    stack = deque()

    current = start_vertex
    traversal_list = []
    while len(vertices) != len(traversal_list):
        print(f"\nCurrent vertex: {current.value}")
        # Visit current vertex
        if current.value not in visited:
            visited.append(current.value)   # Holds strings
            # Add to traversal stack
            stack.appendleft(current)       # Holds vertices
        visited_txt = ", ".join(visited)
        stack_txt = ", ".join([n.value for n in stack])
        print(f"Nodes visited (count = {len(visited)}): {visited_txt}")
        print(f"Nodes on stack (count = {len(stack)}): {stack_txt}")

        # Get unvisited neighbours
        neighbours = [graph.graph_dict[n] for n in current.get_edges() if n not in visited]
        # If current vertex does not have any connected nodes, pop from stack and add value to traversal list
        if len(neighbours) == 0:
            print(f"Adding {stack[0].value} to traveral list")
            traversal_list.append(stack.popleft().value)
            if len(stack) != 0:
                current = stack[0]
                print(f"---- New current vertex: {current.value}")
                stack_txt = ", ".join([n.value for n in stack])
                print(f"---- New nodes on stack (count = {len(stack)}): {stack_txt}")
        # Else, update current to "closest" child e.g. b before e
        else:
            current = min(neighbours) 

    return traversal_list

# Create graph
graph = Graph(True)

# Create vertices
print("Creating vertices...")
vertices_txt = ['a', 'b', 'e', 'f', 'g', 'h']
vertices = [Vertex(v) for v in vertices_txt]
print("Created: " + ", ".join([v.value for v in vertices]))

# Add vertices to graph
print("\nAdding vertices to graph...")
for vertex in vertices:
    graph.add_vertex(vertex)

# Create edges
a, b, e, f, g, h = graph.graph_dict['a'], graph.graph_dict['b'], graph.graph_dict['e'], graph.graph_dict['f'], graph.graph_dict['g'], graph.graph_dict['h'] 
print("\nConnecting edges...")
graph.add_edge(a, b)
graph.add_edge(a, e)
graph.add_edge(a, f)
graph.add_edge(b, f)
graph.add_edge(b, g)
graph.add_edge(e, f)
graph.add_edge(g, h)

# Print connected graph
print("\n=================================")
print("Graph Printout")
print("=================================")
print_graph(graph)

# Print DFS post-order and topological order sort
print("\n=================================")
print("Graph DFS Traversal")
print("=================================")
sorted_order = dfs_post_order(graph, a)
post_order_txt = " > ".join(sorted_order)
print("\nDFS Postorder Traversal Order: " + post_order_txt)
sorted_order_2 = sorted_order.copy()
sorted_order_2.reverse()
topological_order_txt = " > ".join(sorted_order_2)
print("DFS Topological Traversal Order: " + topological_order_txt)
print()
