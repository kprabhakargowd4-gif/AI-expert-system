# Vacuum Cleaner Agent for 2x2 Grid

# Initial grid: 1 = dirty, 0 = clean
grid = [
    [1, 0],
    [1, 1]
]

# Starting position of the vacuum cleaner
position = [0, 0]

def print_grid(grid):
    for row in grid:
        print(row)
    print()

def is_clean(grid):
    for row in grid:
        if 1 in row:
            return False
    return True

def vacuum_cleaner(grid, position):
    actions = 0
    print("Initial Environment:")
    print_grid(grid)
    
    while not is_clean(grid):
        x, y = position
        # If dirty, clean it
        if grid[x][y] == 1:
            print(f"Cleaning cell ({x},{y})")
            grid[x][y] = 0
            actions += 1
        else:
            print(f"Cell ({x},{y}) is already clean")
        
        # Move to next position
        if y < len(grid[0]) - 1:
            position = [x, y + 1]
        elif x < len(grid) - 1:
            position = [x + 1, 0]
        else:
            break  # All cells checked
    
    print("\nFinal Environment (All Clean):")
    print_grid(grid)
    print(f"Total actions performed: {actions}")

# Run the vacuum cleaner
vacuum_cleaner(grid, position)
