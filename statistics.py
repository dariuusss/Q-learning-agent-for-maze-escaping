import labyrinth as maze
import multiply as mp
import q_learning as ql
import path

def max_size(my_list):
    size = len(my_list)
    idx = 0
    for i in range(1,size,1):
        if(len(my_list[i]) > len(my_list[idx])):
            idx = i

    return len(my_list[idx])


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
            if best_path[-1] == finish[i]:
                optimal_paths[i].append(best_path)
                paths -= 1


    for i in range(size):
        biggest_len = max_size(optimal_paths[i])
        optimal_paths[i] = list(filter(lambda p: len(p) == biggest_len, optimal_paths[i]))

    print("Statistics:\n")
    for i in range(size):
        print(f"Robot {i + 1} discovered {len(optimal_paths[i])} optimal paths of length {len(optimal_paths[i][0])}:\n")
        for j in range(len(optimal_paths[i])):
            print(optimal_paths[i][j])
        print("")