import asr
import numpy as np
import random

def find_best_path(start,finish,labyrinth,Q):
    state = start
    path = [state]
    visited = set()
    score_list = [0]
    score = 0
    while state != finish:
        visited.add(state)
        actions = asr.possible_actions(labyrinth,state, visited)
        if not actions:  # No valid actions left
            break
        action = np.argmax(Q[state[0], state[1]])
        if action not in actions:
            action = random.choice(actions) # Fall back to a valid action if the chosen action is invalid
        x, y = state[0], state[1]
        score = score + Q[state[0], state[1],action]
        score_list.append(score)
        state = asr.next_state(state, action)
        path.append(state)
    return (path,score,labyrinth,score_list)


def print_path(path):
    i = 0
    j = len(path)
    while i < j and path[i] != '#':
        i = i + 1
    print(path[:i])

