import labyrinth as maze
import q_learning as ql
import multiply as mp
import path

labyrinth = maze.initialise_labyrinth();
maze.fill_labyrinth(labyrinth)

mp.initialise_multipliers()

start = (0, 0)
finish = (7, 7)

gamma = 0.9  # discount factor
alpha = 0.8  # learning rate
epsilon = 0.9

Q_table = ql.q_learning(labyrinth,start,finish,epsilon,alpha,gamma)

best_path = path.find_best_path(start,finish,labyrinth,Q_table)
print(best_path)
