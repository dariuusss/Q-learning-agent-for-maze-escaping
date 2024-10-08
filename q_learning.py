import random
import numpy as np
import asr
import mp

visited = None
def q_learning(labyrinth,start,finish,epsilon,alpha,gamma,total_episodes,decay_rate):

    Q = np.zeros((labyrinth.shape[0], labyrinth.shape[1], 4))  # 4 directions

    # 0 = up ;; 1 = down ;; 2 = left ;; 3 = right
    global visited
    for episode in range(total_episodes):
        mp.initialise_multipliers()
        current_state = start
        visited = set()
        while current_state != finish:
            visited.add(current_state)
            actions = asr.possible_actions(labyrinth,current_state, visited)
            if not actions:  # No valid actions left
                break
            if random.uniform(0, 1) < epsilon:
                action = random.choice(actions)  # Explore
            else:
                action = np.argmax(Q[current_state[0], current_state[1]])  # Exploit
                if action not in actions:
                    action = random.choice(actions)  # Fall back to exploration if the action is invalid

            the_next_state = asr.next_state(current_state, action)

            instant_reward = asr.reward(labyrinth,current_state, action)

            old_value = Q[current_state[0], current_state[1], action]
            next_max = np.max(Q[the_next_state[0], the_next_state[1]])

            new_value = old_value + alpha * (instant_reward + gamma * next_max - old_value)
            Q[current_state[0], current_state[1], action] = new_value

            current_state = the_next_state

        epsilon *= (1 - decay_rate)

    return Q
