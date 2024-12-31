from normal.road_network import create_graph, visualize_graph
from normal.agent import traverse_all_cities

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

# Pick a random start city
import random
start_city = random.choice(list(roads.keys()))
print(f"Starting city: {start_city}")

# Traverse all cities
traversal_path = traverse_all_cities(roads, start_city, strategy='bfs')
print("Traversal Path:", traversal_path)

# Visualize the traversal
visualize_graph(G, traversal_path)
