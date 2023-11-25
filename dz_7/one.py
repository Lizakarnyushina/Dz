from collections import deque

def bfs(graph, start, target):
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        node, distance = queue.popleft()
        if node == target:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))

    return None