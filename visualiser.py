import numpy as np
import matplotlib.pyplot as plt
from tkinter import simpledialog
import tkinter as tk

steps = 4
interval = 0.01
matrix = np.random.rand(8, 8)  # O matrice 8x8 cu valori aleatorii
coordinates = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3)]

def interpolate_coordinates(start, end, steps):
    """Generează coordonatele intermediare între două puncte."""
    x_coords = np.linspace(start[1], end[1], steps)
    y_coords = np.linspace(start[0], end[0], steps)
    return list(zip(y_coords, x_coords))

def plot_live_maze(matrix, coordinates, interval, steps):
    """Afișează matricea și animă mișcarea între coordonatele date."""
    plt.figure(figsize=(19.1, 11))  # Dimensiune mare pentru figura

    for i in range(len(coordinates) - 1):
        start = coordinates[i]
        end = coordinates[i + 1]

        interpolated_coords = interpolate_coordinates(start, end, steps)

        for lin, col in interpolated_coords:
            plt.clf()  # Curăță figura pentru următoarea actualizare
            plt.imshow(matrix, cmap='Blues', interpolation='nearest', aspect='auto')

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

def start():
    global steps
    global interval
    global matrix
    global coordinates
    # Creează fereastra principală
    root = tk.Tk()
    root.withdraw()  # Ascunde fereastra principală

    user_input = simpledialog.askinteger("Input", "Ce robot doriți să urmăriți? (1-4)", minvalue=1, maxvalue=4)

    # Apelarea funcției de plotare
    plot_live_maze(matrix, coordinates, interval, steps)


