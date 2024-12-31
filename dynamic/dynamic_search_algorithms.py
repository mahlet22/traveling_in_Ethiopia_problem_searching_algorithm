from collections import deque
import heapq
def bfs_traverse_all(G, start_city):
    visited = set()
    traversal_path = []
    queue = deque([start_city])

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        traversal_path.append(current)

        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                queue.append(neighbor)

    return traversal_path



def k_shortest_paths(G, start, goal, k):
    """
    Find the k-shortest paths between two cities in a weighted graph.

    Parameters:
        G (nx.Graph): The graph.
        start (str): Starting city.
        goal (str): Goal city.
        k (int): Number of shortest paths to find.

    Returns:
        List[Tuple[float, List[str]]]: A list of tuples containing the path cost and the path.
    """
    # Priority queue: stores (path cost, current node, path taken)
    queue = [(0, start, [start])]
    paths = []
    visited_paths = set()

    while queue and len(paths) < k:
        cost, current, path = heapq.heappop(queue)

        # If the goal is reached, add the path to the result
        if current == goal:
            if tuple(path) not in visited_paths:
                paths.append((cost, path))
                visited_paths.add(tuple(path))
            continue

        # Expand neighbors
        for neighbor, weight in G[current].items():
            if neighbor not in path:  # Avoid cycles
                total_cost = cost + weight['weight']
                heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))

    return paths
