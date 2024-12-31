import networkx as nx
import matplotlib.pyplot as plt

def create_graph(roads):
    G = nx.Graph()
    for city, neighbors in roads.items():
        for neighbor, distance in neighbors:
            G.add_edge(city, neighbor, weight=distance)
    return G

def visualize_graph(G, path=None):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=10)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if path:
        edges_in_path = [(path[i], path[i+1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=2)

    plt.show()
