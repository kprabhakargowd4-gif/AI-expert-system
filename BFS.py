from collections import deque

# Goal configuration
goal_state = [[1,2,3],[4,5,6],[7,8,0]]

def to_tuple(state):
    return tuple(tuple(row) for row in state)

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)

def get_neighbors(state):
    i, j = find_blank(state)
    moves = []
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            moves.append(new_state)
    return moves

def bfs(start):
    queue = deque([(start, [])])
    visited = set()
    visited.add(to_tuple(start))

    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path + [state]
        for neighbor in get_neighbors(state):
            t = to_tuple(neighbor)
            if t not in visited:
                visited.add(t)
                queue.append((neighbor, path + [state]))
    return None

# Example usage
start_state = [[1,2,3],
               [4,0,6],
               [7,5,8]]

solution = bfs(start_state)

if solution:
    print(f"✅ Solution found in {len(solution)-1} moves.\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("❌ No solution found.")
