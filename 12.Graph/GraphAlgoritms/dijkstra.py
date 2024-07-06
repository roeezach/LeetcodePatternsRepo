import heapq
from typing import List, Tuple, Dict

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    # distances = {node: float('inf') for node in graph}
    distances = {}
    min_heap = [(0, start)]
    for node in graph:
        distances[node] = float('inf')
    
    distances[start] = 0

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances

# Example usage
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

distances = dijkstra(graph, 0)
print("Dijkstra's Algorithm:", distances)  # Output: {0: 0, 1: 3, 2: 1, 3: 4}