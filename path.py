import asr
import numpy as np
import random

def find_best_path(start,finish,labyrinth,Q):
    state = start
    path = [state]
    visited = set()
    while state != finish:
        visited.add(state)
        actions = asr.possible_actions(labyrinth,state, visited)
        if not actions:  # No valid actions left
            break
        action = np.argmax(Q[state[0], state[1]])
        if action not in actions:
            action = random.choice(actions)  # Fall back to a valid action if the chosen action is invalid
        state = asr.next_state(state, action)
        path.append(state)
    return path
