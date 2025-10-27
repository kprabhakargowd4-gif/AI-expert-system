# Backward Chaining Example in Python

# Knowledge Base
rules = {
    "wet_grass": ["raining"],              # If raining then wet_grass
    "slippery": ["wet_grass"],             # If wet_grass then slippery
    "raining": []                          # raining is a fact (no antecedents)
}

# Function for backward chaining
def backward_chaining(goal, inferred=None):
    if inferred is None:
        inferred = set()

    # If the goal is already inferred
    if goal in inferred:
        return True

    # If the goal is not in rules (unknown fact)
    if goal not in rules:
        return False

    # If goal has no antecedents (is a known fact)
    if not rules[goal]:
        inferred.add(goal)
        return True

    # Otherwise, check if all antecedents are true
    for condition in rules[goal]:
        if not backward_chaining(condition, inferred):
            return False

    inferred.add(goal)
    return True

# Main Program
goal = "slippery"

print(f"🎯 Goal: Is the grass '{goal}'?")
result = backward_chaining(goal)

if result:
    print(f"✅ The goal '{goal}' is TRUE (proved by backward chaining).")
else:
    print(f"❌ The goal '{goal}' cannot be proved.")
