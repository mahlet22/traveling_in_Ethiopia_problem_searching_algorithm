from dynamic.dynamic_road_network import create_graph, visualize_k_shortest_paths
from dynamic.dynamic_search_algorithms import k_shortest_paths

# Define the road network
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

# Create the graph
G = create_graph(roads)

# Define start and goal cities
start_city = 'Addis Ababa'
goal_city = 'Mekelle'

# Number of shortest paths to find
k = 3

# Find k-shortest paths
shortest_paths = k_shortest_paths(G, start_city, goal_city, k)
print(f"The {k}-shortest paths from {start_city} to {goal_city} are:")
for idx, (cost, path) in enumerate(shortest_paths, 1):
    print(f"Path {idx}: {path} with cost {cost}")

# Visualize the k-shortest paths
visualize_k_shortest_paths(G, shortest_paths)
