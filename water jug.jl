# Water Jug Problem using Depth First Search (DFS)

MAX_JUG1 = 4  # Capacity of first jug
MAX_JUG2 = 3  # Capacity of second jug
goal = 2      # Desired amount in the 4-gallon jug

visited = set()  # To keep track of visited states

def dfs(x, y, path):
    # If this state is already visited, skip it
    if (x, y) in visited:
        return False
    visited.add((x, y))

    # Add current state to path
    path.append((x, y))

    # Goal check
    if x == goal:
        print("✅ Solution found:")
        for step in path:
            print(f"Jug1: {step[0]} gallons, Jug2: {step[1]} gallons")
        print()
        return True

    # Possible operations:
    moves = []

    # 1. Fill Jug1
    moves.append((MAX_JUG1, y))
    # 2. Fill Jug2
    moves.append((x, MAX_JUG2))
    # 3. Empty Jug1
    moves.append((0, y))
    # 4. Empty Jug2
    moves.append((x, 0))
    # 5. Pour Jug1 → Jug2
    pour = min(x, MAX_JUG2 - y)
    moves.append((x - pour, y + pour))
    # 6. Pour Jug2 → Jug1
    pour = min(y, MAX_JUG1 - x)
    moves.append((x + pour, y - pour))

    # Explore all next states (DFS)
    for (new_x, new_y) in moves:
        if dfs(new_x, new_y, path.copy()):  # Recursive DFS call
            return True

    return False

def water_jug_dfs():
    print("💧 Solving Water Jug Problem using DFS...\n")
    if not dfs(0, 0, []):
        print("❌ No solution found.")

# Run the program
water_jug_dfs()
