import heapq
import math

# Graph (Node connections + distances)
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'D': 4, 'E': 1},
    'C': {'F': 2},
    'D': {'G': 2},
    'E': {'G': 3},
    'F': {'G': 1},
    'G': {}
}

# Heuristic (Straight-line to goal G)
heuristic = {
    'A': 7, 'B': 6, 'C': 4,
    'D': 4, 'E': 2, 'F': 1, 'G': 0
}

# Beam Search Function
def beam_search(start, goal, k):
    frontier = [(heuristic[start], start, [start])]
    while frontier:
        new_frontier = []
        for (_, current, path) in frontier:
            if current == goal:
                return path
            for neighbor in graph[current]:
                new_path = path + [neighbor]
                heapq.heappush(new_frontier, (heuristic[neighbor], neighbor, new_path))
        frontier = heapq.nsmallest(k, new_frontier)  # Keep only top k
    return None

# BFS for comparison
from collections import deque

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# Run Both Searches
start, goal, k = 'A', 'G', 2
beam_result = beam_search(start, goal, k)
bfs_result = bfs(start, goal)

print("Beam Search Path:", beam_result)
print("BFS Path:", bfs_result)
