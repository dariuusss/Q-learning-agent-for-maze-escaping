import numpy as np

def fill_labyrinth(start,finish):
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
    labyrinth[0][5] = 1
    labyrinth[2][2] = 2
    labyrinth[4][1] = 4
    labyrinth[1][2] = -1000000
    labyrinth[3][3] = -1000000
    labyrinth[7][4] = -1000000
    labyrinth[6][7] = -1000000
    labyrinth[5][2] = 5
    labyrinth[4][6] = 6
    used_values = (1, 2, 4, 5, 6)
    for i in range(8):
        for j in range(8):
            if labyrinth[i][j] == 0:
                labyrinth[i][j] = (pow(j + 2 * i + 1, (i + j) % 3) * 10 + 8) * 10 + 10

    i,j = start
    labyrinth[i][j] = 0
    i,j = finish
    labyrinth[i][j] = 100000
    return labyrinth
