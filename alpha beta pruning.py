import math

# Alpha-Beta Pruning Function
def alpha_beta(depth, node_index, is_max, scores, alpha, beta, max_depth):
    # Base Case: If leaf node, return its value
    if depth == max_depth:
        return scores[node_index]

    if is_max:
        best = -math.inf
        # Explore left and right child nodes
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, False, scores, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth} for MAX node")
                break
        return best

    else:
        best = math.inf
        # Explore left and right child nodes
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, True, scores, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth} for MIN node")
                break
        return best


# Driver Code
scores = [3, 5, 6, 9, 1, 2, 0, -1]  # Leaf node values
max_depth = 3  # Tree depth = log2(len(scores))

print("Leaf node scores:", scores)
best_value = alpha_beta(0, 0, True, scores, -math.inf, math.inf, max_depth)

print(f"\n✅ The optimal value (best score for MAX) is: {best_value}")
