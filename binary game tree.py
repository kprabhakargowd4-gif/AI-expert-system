# Binary Game Tree using Minimax Algorithm

# Function to apply minimax
def minimax(depth, node_index, is_maximizing, scores, height):
    # If leaf node is reached, return its score
    if depth == height:
        return scores[node_index]
    
    # If it's the maximizer's move
    if is_maximizing:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    else:
        # Minimizer's move
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )

# Example leaf node values
scores = [3, 5, 2, 9]   # values at leaf nodes

# Height of the tree (log2 of number of leaf nodes)
import math
tree_height = math.log2(len(scores))

# Compute the optimal value
optimal_value = minimax(0, 0, True, scores, int(tree_height))
print("Optimal value for the AI (root node):", optimal_value)
