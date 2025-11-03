from itertools import permutations

# Travelling Salesman Problem using brute force

# Distance matrix (symmetric graph)
# A, B, C, D
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Number of cities
n = len(graph)
cities = list(range(n))

# Starting city
start = 0
min_cost = float('inf')
best_path = None

# Generate all possible routes (permutations)
for perm in permutations(cities):
    if perm[0] != start:
        continue  # Always start from city 0
    
    cost = 0
    for i in range(n - 1):
        cost += graph[perm[i]][perm[i + 1]]
    cost += graph[perm[-1]][start]  # Return to start city

    if cost < min_cost:
        min_cost = cost
        best_path = perm

# Display result
print("Shortest Path:", ' → '.join(chr(65 + i) for i in best_path), "→ A")
print("Minimum Cost:", min_cost)
