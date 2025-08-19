import heapq

def greedy_best_first_search(graph, heuristics, start, goal):
    # Priority queue with (heuristic, node)
    open_list = [(heuristics[start], start)]
    visited = set()
    parent = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            # reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    parent[neighbor] = current
                    heapq.heappush(open_list, (heuristics[neighbor], neighbor))
    return None


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Heuristic values (example — like straight-line distance to goal)
heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 3,
    'F': 1,
    'G': 0
}

start, goal = 'A', 'G'
path = greedy_best_first_search(graph, heuristics, start, goal)
print("Path found:", path)
