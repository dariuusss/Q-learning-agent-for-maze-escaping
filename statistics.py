import labyrinth as maze
import mp
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

def analysis(start,finish,gamma,alpha,epsilon,total_episodes,decay_rate):

    size = len(start)
    optimal_paths = [[],[],[],[]]

    for i in range(size):
        labyrinth = maze.fill_labyrinth(start[i], finish[i])
        paths = 3

        while paths > 0:
            Q_table = ql.q_learning(labyrinth, start[i], finish[i], epsilon, alpha, gamma,total_episodes,decay_rate)
            best_path = path.find_best_path(start[i], finish[i], labyrinth, Q_table)
            if (best_path[0])[-1] == finish[i]:
                for t in range(mp.still_rounds):
                    best_path[0].append('#')
                optimal_paths[i].append(best_path)
                paths -= 1


    for i in range(size):
        optimal_paths[i] = sorted(optimal_paths[i], key= lambda x: x[1].item() / len(x[0]), reverse = True )[: 1]

    print("Statistics:\n")
    for i in range(size):
        print(f"Robot {i + 1}'s discovered optimal path:\n")
        path.print_path((optimal_paths[i][0])[0])
        print("")

    user_answer = None
    while user_answer != "NO" and user_answer != "no":
        user_answer = simpledialog.askstring("Input", "Doriti vizualizare in timp real? (YES/NO)")
        if user_answer == "YES" or user_answer == "yes":
            idx = simpledialog.askinteger("Input", "Ce robot doriți să urmăriți? (1-4)", minvalue=1, maxvalue=4) - 1
            visualiser.plot_live_maze((optimal_paths[idx][0])[2],(optimal_paths[idx][0])[0],0.02,5)
