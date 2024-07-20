import numpy as np
import random

labyrinth = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
])


def fill_labyrinth(labyrinth):
    labyrinth[0][5] = 1
    labyrinth[2][2] = 2
    labyrinth[4][1] = 4
    labyrinth[1][2] = -100000
    labyrinth[3][3] = -100000
    labyrinth[7][4] = -100000
    labyrinth[6][7] = -100000
    labyrinth[7][7] = 10000
    labyrinth[5][2] = 5
    labyrinth[4][6] = 6
    used_values = (1, 2, 4, 5, 6, 10000)
    for i in range(8):
        for j in range(8):
            if labyrinth[i][j] == 0:
                if labyrinth[i][j] in used_values:
                    labyrinth[i][j] = pow(j + 2 * i + 1, (i + j) % 3)
                else:
                    labyrinth[i][j] = pow(j + 2 * i + 1, (i + j) % 3) * 10 + 8
    labyrinth[0,0] = 0


fill_labyrinth(labyrinth)

multipliers = (1, 2, 4, 5, 6)
multipliers_map = {
    1: 0.25,
    2: 0.5,
    4: 0.75,
    5: 1.5,
    6: 1.25
}
multiplier = 1

start = (0, 0)
finish = (7, 7)

gamma = 0.9  # discount factor
alpha = 0.8  # learning rate
epsilon = 0.9

Q = np.zeros((labyrinth.shape[0], labyrinth.shape[1], 4))  # 4 directions


# 0 = up ;; 1 = down ;; 2 = left ;; 3 = right

def possible_actions(current_state, visited):  # current_state is a tuple of coordinates
    actions = []
    row = current_state[0]
    column = current_state[1]
    if row > 0 and (row - 1, column) not in visited:
        actions.append(0)
    if row + 1 < labyrinth.shape[0] and (row + 1, column) not in visited:
        actions.append(1)
    if column > 0 and (row, column - 1) not in visited:
        actions.append(2)
    if column + 1 < labyrinth.shape[1] and (row, column + 1) not in visited:
        actions.append(3)
    return actions


def next_state(current_state, action):
    row = current_state[0]
    column = current_state[1]
    if action == 0:
        return (row - 1, column)
    if action == 1:
        return (row + 1, column)
    if action == 2:
        return (row, column - 1)
    if action == 3:
        return (row, column + 1)
    return current_state  # return current state if no valid action


def reward(current_state, action):
    global multiplier
    global multipliers
    global multipliers_map

    i = current_state[0]
    j = current_state[1]
    x = labyrinth[i, j]
    the_next_state = next_state(current_state, action)
    ii = the_next_state[0]
    jj = the_next_state[1]
    y = labyrinth[ii, jj]

    if x not in multipliers and y not in multipliers:
        return_value = multiplier * y
        multiplier = 1
        return return_value

    if x not in multipliers and y in multipliers:
        multiplier *= multipliers_map[y]
        return 0

    if x in multipliers and y in multipliers:
        multiplier = multiplier * multipliers_map[x]
        return 0

    if x in multipliers and y not in multipliers:
        return_value = multipliers_map[x] * multiplier * y
        multiplier = 1
        return return_value


def q_learning():
    global epsilon
    global alpha
    for episode in range(100):
        current_state = start
        visited = set()
        steps = 0
        while current_state != finish:
            visited.add(current_state)
            actions = possible_actions(current_state, visited)
            if not actions:  # No valid actions left
                break
            if random.uniform(0, 1) < epsilon:
                action = random.choice(actions)  # Explorare
            else:
                action = np.argmax(Q[current_state[0], current_state[1]])  # Exploatare
                if action not in actions:
                    action = random.choice(actions)  # Fall back to exploration if the action is invalid

            the_next_state = next_state(current_state, action)

            instant_reward = reward(current_state, action)

            old_value = Q[current_state[0], current_state[1], action]
            next_max = np.max(Q[the_next_state[0], the_next_state[1]])

            new_value = old_value + alpha * (instant_reward + gamma * next_max - old_value)
            Q[current_state[0], current_state[1], action] = new_value

            current_state = the_next_state
            steps += 1

        epsilon *= 0.5


q_learning()


def find_best_path():
    state = start
    path = [state]
    visited = set()
    while state != finish:
        visited.add(state)
        actions = possible_actions(state, visited)
        if not actions:  # No valid actions left
            break
        action = np.argmax(Q[state[0], state[1]])
        if action not in actions:
            action = random.choice(actions)  # Fall back to a valid action if the chosen action is invalid
        state = next_state(state, action)
        path.append(state)
    return path


path = find_best_path()
print(path)
