import numpy as np
import matplotlib.pyplot as plt

def interpolate_coordinates(start, end, steps):
    """Generează coordonatele intermediare între două puncte."""
    x_coords = np.linspace(start[1], end[1], steps)
    y_coords = np.linspace(start[0], end[0], steps)
    return list(zip(y_coords, x_coords))

def highlight_matrix_live(matrix, coordinates, interval=0.05, steps=1):
    """Afișează matricea și animă mișcarea între coordonatele date."""
    plt.figure(figsize=(6, 6))

    for i in range(len(coordinates) - 1):
        start = coordinates[i]
        end = coordinates[i + 1]

        # Obține coordonatele intermediare
        interpolated_coords = interpolate_coordinates(start, end, steps)

        for lin, col in interpolated_coords:
            plt.clf()  # Curăță figura pentru următoarea actualizare
            plt.imshow(matrix, cmap='Blues', interpolation='nearest')

            # Evidențierea elementului curent cu roșu
            plt.scatter(col, lin, s=500, color='red', edgecolor='black')

            plt.xticks(range(matrix.shape[1]))
            plt.yticks(range(matrix.shape[0]))

            plt.title(f'Mișcare de la ({start[0]},{start[1]}) la ({end[0]},{end[1]})')
            plt.grid(True, which='both', color='gray', linewidth=0.5)

            plt.pause(interval)  # Pauză pentru a permite vizualizarea mișcării

    plt.show()

# Exemplu de utilizare
matrix = np.random.rand(8, 8)  # O matrice 8x8 cu valori aleatorii
coordinates = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3)]

# Afișăm imaginile în timp real
highlight_matrix_live(matrix, coordinates, interval=0.01, steps=10)
