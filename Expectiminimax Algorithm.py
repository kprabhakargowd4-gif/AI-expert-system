# Expectiminimax Algorithm for a Stochastic Game Tree

def expectiminimax(node, player):
    """
    player = 'MAX' for maximizing player
    player = 'MIN' for minimizing player
    player = 'CHANCE' for random event
    """

    # Base Case: If node is a terminal node
    if isinstance(node, int):  # Leaf nodes are just numbers
        return node

    # MAX player's turn
    if player == "MAX":
        best_value = float('-inf')
        for child in node:
            val = expectiminimax(child, "MIN")
            best_value = max(best_value, val)
        return best_value

    # MIN player's turn
    elif player == "MIN":
        best_value = float('inf')
        for child in node:
            val = expectiminimax(child, "CHANCE")
            best_value = min(best_value, val)
        return best_value

    # CHANCE node (Random Event)
    else:  # player == "CHANCE"
        probability = 1 / len(node)  # Equal probability for all outcomes
        expected_value = 0
        for child in node:
            expected_value += probability * expectiminimax(child, "MAX")
        return expected_value


# Example Game Tree
game_tree = [
    [3, 12, 8],          # MAX → MIN → VALUES
    [2, 4, 6],           # Another branch
    [
        [14, 5],         # CHANCE Node → MAX → MIN
        [2, 10]
    ]
]

# Run Algorithm from the root
result = expectiminimax(game_tree, "MAX")
print("Optimal Expected Value for MAX Player:", result)
