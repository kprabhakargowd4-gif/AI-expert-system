# Map Coloring Problem using Backtracking

# Define the map as a graph
# Each key is a region, and its values are the neighboring regions
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'C', 'E'],
    'E': ['B', 'C', 'D']
}

# Available colors
colors = ['Red', 'Green', 'Blue', 'Yellow']

# Store color assignment
assigned_colors = {}

def is_safe(region, color):
    for neighbor in graph[region]:
        if neighbor in assigned_colors and assigned_colors[neighbor] == color:
            return False
    return True

def color_map(region_list, index=0):
    if index == len(region_list):
        return True  # All regions colored successfully
    
    region = region_list[index]
    for color in colors:
        if is_safe(region, color):
            assigned_colors[region] = color
            if color_map(region_list, index + 1):
                return True
            assigned_colors.pop(region)  # Backtrack
    
    return False

# Driver code
region_list = list(graph.keys())

if color_map(region_list):
    print("✅ Map coloring successful!\n")
    for region in assigned_colors:
        print(f"Region {region} → {assigned_colors[region]}")
else:
    print("❌ No valid coloring possible.")
