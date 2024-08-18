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

    labyrinth[1][2] = -10000000
    labyrinth[3][3] = -10000000
    labyrinth[7][4] = -10000000
    labyrinth[6][7] = -10000000
    # 15-18: bombs
    labyrinth[0][5] = 1
    labyrinth[2][2] = 2
    labyrinth[4][1] = 4
    labyrinth[5][2] = 5
    labyrinth[4][6] = 6
    # 20-24: multipliers
    labyrinth[6][3] = 11
    labyrinth[2][5] = 12
    labyrinth[7][6] = 13
    labyrinth[1][1] = 14
    labyrinth[3][6] = 15
    # 26-30: penalties
    labyrinth[4][7] = 16
    # 32: enables revisiting previous cells
    for i in range(labyrinth.shape[0]):
        for j in range(labyrinth.shape[1]):
            if labyrinth[i][j] == 0:
                labyrinth[i][j] = (pow(j + 2 * i + 1, (i + j) % 3) * 10 + 8) * 10 + 17

    i,j = start
    labyrinth[i][j] = 0
    i,j = finish
    labyrinth[i][j] = 1000000
    return labyrinth
