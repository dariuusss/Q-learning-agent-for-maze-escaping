import matplotlib
matplotlib.use('TkAgg')  # Specifică backend-ul
import numpy as np
import matplotlib.pyplot as plt

def highlight_matrix_live(matrix, coordinates, interval = 0.8):
    plt.figure(figsize=(6, 6))

    for idx, (lin, col) in enumerate(coordinates):
        plt.clf()  # Curăță figura pentru următoarea actualizare
        plt.imshow(matrix, cmap='Blues', interpolation='nearest')

        # Evidențierea elementului curent cu roșu
        plt.scatter(col, lin, s=500, color='red', edgecolor='black')

        plt.xticks(range(matrix.shape[1]))
        plt.yticks(range(matrix.shape[0]))

        plt.title(f'Pasul {idx + 1}: Coordonată ({lin},{col})')
        plt.grid(True, which='both', color='gray', linewidth=0.5)

        plt.pause(interval)  # Pauză pentru a permite vizualizarea înainte de actualizarea la următoarea imagine

    plt.show()

# Exemplu de utilizare
matrix = np.random.rand(8, 8)  # O matrice 8x8 cu valori aleatorii
coordinates = [(0, 0), (1, 2), (3, 4), (7, 7), (5, 5), (6, 1), (2, 3), (4, 4), (1, 6), (0, 7)]

# Afișăm imaginile în timp real
highlight_matrix_live(matrix, coordinates)
