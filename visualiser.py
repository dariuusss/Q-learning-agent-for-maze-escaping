import numpy as np
import matplotlib.pyplot as plt

def interpolate_coordinates(start, end, steps):
    """Generează coordonatele intermediare între două puncte."""
    x_coords = np.linspace(start[1], end[1], steps)
    y_coords = np.linspace(start[0], end[0], steps)
    return list(zip(y_coords, x_coords))


def plot_live_maze(matrix, coordinates, interval, steps):
    """Afișează matricea și animă mișcarea între coordonatele date."""
    plt.figure(figsize=(19.1, 11))  # Dimensiune mare pentru figura

    # Matricea de stare, inițial toată albă
    state_matrix = np.ones(matrix.shape)

    for i in range(len(coordinates) - 1):
        start = coordinates[i]
        end = coordinates[i + 1]

        interpolated_coords = interpolate_coordinates(start, end, steps)

        for lin, col in interpolated_coords:
            plt.clf()  # Curăță figura pentru următoarea actualizare

            # Actualizează matricea de stare
            state_matrix[int(lin), int(col)] = 0  # 0 pentru verde, 1 pentru alb

            # Afișează matricea cu culori bazate pe starea celulelor
            plt.imshow(state_matrix, cmap='Greens', interpolation='nearest', aspect='auto')

            # Evidențierea elementului curent cu roșu
            plt.scatter(col, lin, s=500, color='red', edgecolor='black')

            # Afișează valorile fiecărei casete din matrice
            for (i, j), value in np.ndenumerate(matrix):
                plt.text(j, i, f'{value:.2f}', color='black', ha='center', va='center', fontsize=20)

            plt.xticks(range(matrix.shape[1]))
            plt.yticks(range(matrix.shape[0]))

            # Setează limitele axelor pentru a alinia grila
            plt.xlim(-0.5, matrix.shape[1] - 0.5)
            plt.ylim(matrix.shape[0] - 0.5, -0.5)

            # Adaugă linii negre pe marginea fiecărei celule
            for x in range(matrix.shape[1] + 1):
                plt.plot([x - 0.5, x - 0.5], [-0.5, matrix.shape[0] - 0.5], color='black', linewidth=1)

            for y in range(matrix.shape[0] + 1):
                plt.plot([-0.5, matrix.shape[1] - 0.5], [y - 0.5, y - 0.5], color='black', linewidth=1)

            plt.title(f'Mișcare de la ({start[0]},{start[1]}) la ({end[0]},{end[1]})')

            plt.pause(interval)  # Pauză pentru a permite vizualizarea mișcării

    plt.show()
