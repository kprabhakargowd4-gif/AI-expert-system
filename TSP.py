import numpy as np
import random

# Distance matrix (symmetric)
distances = np.array([
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 6],
    [7, 3, 5, 6, 0]
])

num_cities = len(distances)
num_ants = 5
alpha = 1           # Importance of pheromone
beta = 2            # Importance of heuristic
rho = 0.5           # Pheromone evaporation rate
Q = 100             # Constant
iterations = 50

# Initialize pheromones
pheromones = np.ones((num_cities, num_cities))

def probability(i, j, visited):
    if j in visited:
        return 0
    tau = pheromones[i][j] ** alpha
    eta = (1 / distances[i][j]) ** beta
    return tau * eta

def construct_tour(start):
    tour = [start]
    while len(tour) < num_cities:
        i = tour[-1]
        probs = [probability(i, j, tour) for j in range(num_cities)]
        total = sum(probs)
        if total == 0:
            next_city = random.choice([c for c in range(num_cities) if c not in tour])
        else:
            probs = [p / total for p in probs]
            next_city = np.random.choice(range(num_cities), p=probs)
        tour.append(next_city)
    return tour

def tour_length(tour):
    return sum(distances[tour[i]][tour[(i+1) % num_cities]] for i in range(num_cities))

best_tour = None
best_length = float('inf')

for _ in range(iterations):
    all_tours = []
    for ant in range(num_ants):
        start_city = random.randint(0, num_cities - 1)
        tour = construct_tour(start_city)
        all_tours.append(tour)

    # Evaporation
    pheromones *= (1 - rho)

    # Reinforcement
    for tour in all_tours:
        L = tour_length(tour)
        if L < best_length:
            best_length = L
            best_tour = tour
        for i in range(num_cities):
            a = tour[i]
            b = tour[(i+1) % num_cities]
            pheromones[a][b] += Q / L
            pheromones[b][a] += Q / L  # Because undirected

print("\nBest tour found:", best_tour)
print("Best distance:", best_length)
