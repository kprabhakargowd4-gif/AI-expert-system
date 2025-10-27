from heapq import heappush, heappop

# Goal state
goal_state = [[1,2,3],[4,5,6],[7,8,0]]

# Function to find the position of a number
def find_pos(state, num):
    for i in range(3):
        for j in range(3):
            if state[i][j] == num:
                return (i, j)

# Manhattan distance heuristic
def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            num = state[i][j]
            if num != 0:
                x, y = find_pos(goal_state, num)
                dist += abs(x - i) + abs(y - j)
    return dist

# Convert to tuple for hashing
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# Get possible moves
def get_neighbors(state):
    i, j = find_pos(state, 0)
    moves = []
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            moves.append(new_state)
    return moves

def a_star(start):
    pq = []
    heappush(pq, (manhattan(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)
        if state == goal_state:
            return path + [state]
        visited.add(to_tuple(state))
        for neighbor in get_neighbors(state):
            if to_tuple(neighbor) not in visited:
                heappush(pq, (g + 1 + manhattan(neighbor), g + 1, neighbor, path + [state]))
    return None

# Example usage
start_state = [[1,2,3],[4,0,6],[7,5,8]]
solution = a_star(start_state)

if solution:
    print("✅ Solution found in", len(solution)-1, "moves.\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("❌ No solution found.")
