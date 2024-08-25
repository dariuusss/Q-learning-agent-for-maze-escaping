import numpy as np
import matplotlib.pyplot as plt

def interpolate_coordinates(start, end, steps):
    lin_space = np.linspace(start[0], end[0], steps)
    col_space = np.linspace(start[1], end[1], steps)
    return list(zip(lin_space, col_space))

def plot_live_maze(matrix, coordinates, interval, steps):
    plt.figure(figsize=(19.1, 11))

    state_matrix = np.ones(matrix.shape)

    try:
        finish = coordinates.index('#') - 1
    except ValueError:
        finish = len(coordinates) - 1

    for i in range(finish):
        start = coordinates[i]
        end = coordinates[i + 1]

        interpolated_coords = interpolate_coordinates(start, end, steps)

        for lin, col in interpolated_coords:
            plt.clf()
            state_matrix[int(lin), int(col)] = 0  # 0 pentru verde, 1 pentru alb
            plt.imshow(state_matrix, cmap='Greens', interpolation='nearest', aspect='auto')
            plt.scatter(col, lin, s=500, color='red', edgecolor='black')

            for (i, j), value in np.ndenumerate(matrix):
                plt.text(j, i, f'{value:.2f}', color='black', ha='center', va='center', fontsize=20)

            plt.xticks(range(matrix.shape[1]))
            plt.yticks(range(matrix.shape[0]))

            plt.xlim(-0.5, matrix.shape[1] - 0.5)
            plt.ylim(matrix.shape[0] - 0.5, -0.5)

            for x in range(matrix.shape[1] + 1):
                plt.plot([x - 0.5, x - 0.5], [-0.5, matrix.shape[0] - 0.5], color='black', linewidth=1)

            for y in range(matrix.shape[0] + 1):
                plt.plot([-0.5, matrix.shape[1] - 0.5], [y - 0.5, y - 0.5], color='black', linewidth=1)

            plt.title(f'Mișcare de la ({start[0]},{start[1]}) la ({end[0]},{end[1]})')

            plt.pause(interval)

    plt.clf()
    plt.imshow(state_matrix, cmap='Greens', interpolation='nearest', aspect='auto')
    plt.scatter(col, lin, s=500, color='red', edgecolor='black')

    for (i, j), value in np.ndenumerate(matrix):
        plt.text(j, i, f'{value:.2f}', color='black', ha='center', va='center', fontsize=20)

    plt.xticks(range(matrix.shape[1]))
    plt.yticks(range(matrix.shape[0]))

    plt.xlim(-0.5, matrix.shape[1] - 0.5)
    plt.ylim(matrix.shape[0] - 0.5, -0.5)

    for x in range(matrix.shape[1] + 1):
        plt.plot([x - 0.5, x - 0.5], [-0.5, matrix.shape[0] - 0.5], color='black', linewidth=1)

    for y in range(matrix.shape[0] + 1):
        plt.plot([-0.5, matrix.shape[1] - 0.5], [y - 0.5, y - 0.5], color='black', linewidth=1)

    plt.show()
