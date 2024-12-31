from dynamic_search_algorithms import bfs_traverse_all

def traverse_all_cities(G, start_city, strategy='bfs'):
    if strategy == 'bfs':
        return bfs_traverse_all(G, start_city)
    else:
        raise ValueError(f"Strategy {strategy} is not supported!")
