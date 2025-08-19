import heapq

def a_star(graph, heuristics, start, goal):
    open_list = [(heuristics[start], 0, start)]  # (f, g, node)
    parent = {start: None}
    g_cost = {start: 0}

    while open_list:
        _, g, current = heapq.heappop(open_list)

        if current == goal:
            # reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, cost in graph[current]:
            tentative_g = g + cost
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f = tentative_g + heuristics[neighbor]
                parent[neighbor] = current
                heapq.heappush(open_list, (f, tentative_g, neighbor))
    return None


# Example graph with costs
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [],
    'G': []
}

# Heuristics (straight-line distance to G, example values)
heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 4,
    'G': 0
}

start, goal = 'A', 'G'
path = a_star(graph, heuristics, start, goal)
print("Path found:", path)
