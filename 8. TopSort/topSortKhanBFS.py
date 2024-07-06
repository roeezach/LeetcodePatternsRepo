from collections import deque, defaultdict

def topological_sort(num_courses, prerequisites):
    # Create an adjacency list
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    # Build the graph and compute in-degrees of nodes
    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1
    
    # Initialize the queue with nodes having 0 in-degree
    # queue = deque([node for node in range(num_courses) if in_degree[node] == 0])
    queue = deque()
    for node in range(num_courses):
        if in_degree[node] == 0:
            queue.append(node)
    
    top_order = []
    
    while queue:
        node = queue.popleft()
        top_order.append(node)
        
        # Decrease the in-degree of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If top_order contains all nodes, we have a valid topological sort
    if len(top_order) == num_courses:
        return top_order
    else:
        # If there are nodes left with non-zero in-degree, there's a cycle
        return []

# Example usage
num_courses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(topological_sort(num_courses, prerequisites))  # Output: [0, 1, 2, 3] or [0, 2, 1, 3]
