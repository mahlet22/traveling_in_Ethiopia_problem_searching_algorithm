from search_algorithms import bfs_traverse_all

def traverse_all_cities(roads, start_city, strategy='bfs'):
    if strategy == 'bfs':
        return bfs_traverse_all(roads, start_city)
    else:
        raise ValueError(f"Strategy {strategy} is not supported!")
    