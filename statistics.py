import labyrinth as maze
import multiply as mp
import q_learning as ql
import path

def analysis(labyrinth,start,finish,gamma,alpha,epsilon,total_episodes,decay_rate):
    maze.fill_labyrinth(labyrinth, start[0], finish[0])

    mp.initialise_multipliers()

    Q_table = ql.q_learning(labyrinth, start[0], finish[0], epsilon, alpha, gamma,total_episodes,decay_rate)

    best_path = path.find_best_path(start[0], finish[0], labyrinth, Q_table)
    print(best_path)
