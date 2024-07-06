from typing import Dict, List, Tuple


def bellman_ford(graph: List[Tuple[int, int, int]], num_nodes: int, start: int) -> Tuple[Dict[int, int], bool]:
    distances = {}
    for i in range(num_nodes):
        distances[i] = float('inf')
    distances[start] = 0

    for _ in range(num_nodes - 1):
        for u, v, weight in graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative-weight cycles
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return distances, True  # Indicates a negative-weight cycle

    return distances, False

# Example usage
edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5)
]
num_nodes = 4

distances, has_negative_cycle = bellman_ford(edges, num_nodes, 0)
print("Bellman-Ford Algorithm:", distances)  # Output: {0: 0, 1: 3, 2: 1, 3: 4}
print("Contains negative weight cycle:", has_negative_cycle)  # Output: False
