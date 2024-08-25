import mp
import q_learning as ql

#asr stands for actions, states and rewards
def possible_actions(labyrinth,current_state, visited):  # current_state is a tuple of coordinates
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


def reward(labyrinth,current_state, action):

    i = current_state[0]
    j = current_state[1]
    x = labyrinth[i, j]
    the_next_state = next_state(current_state, action)
    ii = the_next_state[0]
    jj = the_next_state[1]
    y = labyrinth[ii, jj]

    if x == 17:
        ql.visited = set()
        labyrinth[i, j] = 0 # at most once to avoid possible infinite loops
        return 0

    if x in mp.penalties:
        mp.still_rounds = mp.still_rounds + x - 10
        return 0

    if x not in mp.multipliers and y not in mp.multipliers:
        return_value = mp.multiplier * y
        mp.multiplier = 1
        return return_value

    if x not in mp.multipliers and y in mp.multipliers:
        mp.multiplier *= mp.multipliers_map[y]
        return 0

    if x in mp.multipliers and y in mp.multipliers:
        mp.multiplier = mp.multiplier * mp.multipliers_map[x]
        return 0

    if x in mp.multipliers and y not in mp.multipliers:
        return_value = mp.multipliers_map[x] * mp.multiplier * y
        mp.multiplier = 1
        return return_value
