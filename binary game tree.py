from collections import deque

def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0):
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True

def successors(state):
    m, c, side = state
    moves = []
    direction = -1 if side == 'L' else 1
    new_side = 'R' if side == 'L' else 'L'
    
    for m_move in range(3):
        for c_move in range(3):
            if 1 <= m_move + c_move <= 2:
                new_m = m + direction * m_move
                new_c = c + direction * c_move
                if is_valid(new_m, new_c):
                    moves.append((new_m, new_c, new_side))
    return moves

def missionaries_and_cannibals():
    start = (3, 3, 'L')
    goal = (0, 0, 'R')
    
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        (state, path) = queue.popleft()
        if state == goal:
            return path
        for next_state in successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    return None

# Run the solver
solution = missionaries_and_cannibals()

# Display the result
if solution:
    print("✅ Solution found:")
    for step in solution:
        print(step)
else:
    print("❌ No solution found.")
