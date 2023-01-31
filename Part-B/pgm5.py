# This program uses a heuristic approach to solve the traveling salesman problem

from random import shuffle

def travel(graph, start):
    # Create a list of vertices to visit
    unvisited = [i for i in range(len(graph))]
    unvisited.remove(start)
    current = start
    path = [start]
    
    # While there are still vertices to visit
    while unvisited:
        # Find the closest unvisited vertex
        closest = min([(graph[current][j], j) for j in unvisited])[1]
        current = closest
        path.append(current)
        unvisited.remove(current)
    
    # Return the path
    return path

# Example graph (adjacency matrix)
graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]

# Shuffle the starting vertex
start = 0
shuffle(graph)

# Get the path
path = travel(graph, start)

# Print the path
print(path)
