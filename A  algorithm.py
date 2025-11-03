from queue import PriorityQueue

# A* Algorithm implementation

def a_star(graph, heuristic, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    g = {start: 0}
    parent = {start: None}

    while not open_list.empty():
        f, current = open_list.get()

        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, g[goal]

        for neighbor, cost in graph[current].items():
            temp_g = g[current] + cost
            temp_f = temp_g + heuristic[neighbor]

            if neighbor not in g or temp_g < g[neighbor]:
                g[neighbor] = temp_g
                parent[neighbor] = current
                open_list.put((temp_f, neighbor))

    return None, float('inf')


# Example graph (weighted)
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 3, 'E': 1},
    'C': {'A': 3, 'F': 5},
    'D': {'B': 3, 'G': 2},
    'E': {'B': 1, 'G': 1},
    'F': {'C': 5, 'G': 2},
    'G': {'D': 2, 'E': 1, 'F': 2}
}

# Heuristic values (estimated distance to goal G)
heuristic = {'A': 7, 'B': 6, 'C': 5, 'D': 3, 'E': 2, 'F': 2, 'G': 0}

path, cost = a_star(graph, heuristic, 'A', 'G')

print("Shortest Path:", path)
print("Total Cost:", cost)
