def dfs(graph, start):
    visited = set()
    result = []
    dfs_visit(graph, start, visited, result)
    return result

def dfs_visit(graph, start, visited, result):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example usage
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1],
    4: [1],
    5: [2],
    6: [2]
}

print(dfs(graph, 0))  # Output: [0, 2, 6, 5, 1, 4, 3]
