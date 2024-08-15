import labyrinth as maze
import multiply as mp
import q_learning as ql
import path
import visualiser
from tkinter import simpledialog

def max_size(my_list):
    size = len(my_list)
    idx = 0
    for i in range(1,size,1):
        if len((my_list[i])[0]) > len((my_list[idx])[0]):
            idx = i

    return len((my_list[idx])[0])


def analysis(labyrinth,start,finish,gamma,alpha,epsilon,total_episodes,decay_rate):

    size = len(start)
    optimal_paths = [[],[],[],[]]

    for i in range(size):
        maze.fill_labyrinth(labyrinth, start[i], finish[i])
        mp.initialise_multipliers()
        paths = 3

        while paths > 0:
            Q_table = ql.q_learning(labyrinth, start[i], finish[i], epsilon, alpha, gamma,total_episodes,decay_rate)
            best_path = path.find_best_path(start[i], finish[i], labyrinth, Q_table)
            if (best_path[0])[-1] == finish[i]:
                optimal_paths[i].append(best_path)
                paths -= 1

    for i in range(size):
        biggest_len = max_size(optimal_paths[i])
        optimal_paths[i] = (sorted( list(filter(lambda p: len(p[0]) == biggest_len, optimal_paths[i])), key=lambda x: x[1].item() / len(x[0]), reverse=True ))[:1]

    print("Statistics:\n")
    for i in range(size):
        print(f"Robot {i + 1} discovered an optimal path of length {len(((optimal_paths[i])[0])[0])} and average score of {optimal_paths[i][0][1].item() / len(optimal_paths[i][0][0])}:\n")
        print((optimal_paths[i][0])[0])
        print("")

    user_answer = None
    while user_answer != "NO" and user_answer != "no":
        user_answer = simpledialog.askstring("Input", "Doriti vizualizare in timp real? (YES/NO)")
        if user_answer == "YES" or user_answer == "yes":
            visualiser.start()