import num py as np
import random

# Grid settings
grid_size = 5
start = (0, 0)
goal = (4, 4)
obstacles = [(1, 2), (3, 3)]

# Q-learning parameters
alpha = 0.7
gamma = 0.9
epsilon = 0.2
episodes = 300

# Actions (Up, Down, Left, Right)
actions = ['U', 'D', 'L', 'R']
Q = np.zeros((grid_size, grid_size, len(actions)))

def get_reward(state):
    if state == goal:
        return 10
    elif state in obstacles:
        return -5
    else:
        return -1  # step penalty

def next_state(state, action):
    x, y = state
    if action == 'U': x = max(0, x - 1)
    if action == 'D': x = min(grid_size - 1, x + 1)
    if action == 'L': y = max(0, y - 1)
    if action == 'R': y = min(grid_size - 1, y + 1)
    return (x, y)

# Training
for _ in range(episodes):
    state = start
    while state != goal:
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)
        else:
            action = actions[np.argmax(Q[state[0], state[1]])]
        
        new_state = next_state(state, action)
        reward = get_reward(new_state)
        
        Q[state[0], state[1], actions.index(action)] += alpha * \
            (reward + gamma * np.max(Q[new_state[0], new_state[1]]) - 
             Q[state[0], state[1], actions.index(action)])
        
        state = new_state

# Optimal Path
state = start
path = [state]
while state != goal:
    action = actions[np.argmax(Q[state[0], state[1]])]
    state = next_state(state, action)
    path.append(state)

print("Learned Q-Table:\n", Q)
print("\nOptimal Path from Start to Goal:")
print(path)
