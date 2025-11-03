from queue import PriorityQueue

def uniform_cost_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, [start]))  # (cost, path)

    while not pq.empty():
        cost, path = pq.get()
        node = path[-1]

        # Goal check
        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    total_cost = cost + edge_cost
                    pq.put((total_cost, path + [neighbor]))

    return None, float('inf')


# Example weighted graph
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 5), ('E', 4)],
    'C': [('F', 6)],
    'D': [('G', 2)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}

path, cost = uniform_cost_search(graph, 'A', 'G')

print("Shortest Path:", " → ".join(path))
print("Total Cost:", cost)
