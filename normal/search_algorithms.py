from collections import deque

def bfs_traverse_all(roads, start_city):
    visited = set()
    traversal_path = []
    queue = deque([start_city])

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        traversal_path.append(current)

        for neighbor, _ in roads.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return traversal_path
