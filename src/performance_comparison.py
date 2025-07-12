import numpy as np
import time
import matplotlib.pyplot as plt
from .matrix_rotation import rotation_x, rotate_vector_matrix
from .quaternion_rotation import Quaternion, quaternion_from_axis_angle, rotate_vector_quaternion

#mesure_temps_rotations_matricielles_90_mult_60_add
def benchmark_matrix_rotation(num_iterations):
    """#mesure_temps_rotations_matricielles_90_mult_60_add
    Mesure le temps d'application de rotations matricielles sur un vecteur.
    """
    v = np.array([1.0, 0.0, 0.0])
    theta = np.pi / 3
    R = rotation_x(theta)
    start = time.time()
    for _ in range(num_iterations):
        v = rotate_vector_matrix(v, R)
    end = time.time()
    return end - start

#mesure_temps_rotations_quaternions_48_mult_24_add
def benchmark_quaternion_rotation(num_iterations):
    """#mesure_temps_rotations_quaternions_48_mult_24_add
    Mesure le temps d'application de rotations par quaternion sur un vecteur.
    """
    v = np.array([1.0, 0.0, 0.0])
    theta = np.pi / 3
    q = quaternion_from_axis_angle([1, 0, 0], theta)
    start = time.time()
    for _ in range(num_iterations):
        v = rotate_vector_quaternion(v, q)
    end = time.time()
    return end - start

#comparaison_complete_temps_execution
def compare_methods():
    """#comparaison_complete_temps_execution
    Compare les temps d'exécution des deux méthodes pour différents nombres d'itérations.
    """
    iterations = [10**i for i in range(1, 6)]
    times_matrix = [benchmark_matrix_rotation(n) for n in iterations]
    times_quat = [benchmark_quaternion_rotation(n) for n in iterations]
    return iterations, times_matrix, times_quat

#graphique_comparaison_performances
def plot_performance_results():
    """#graphique_comparaison_performances
    Affiche un graphique comparant les performances des deux méthodes.
    """
    iterations, times_matrix, times_quat = compare_methods()
    plt.figure(figsize=(8, 5))
    plt.plot(iterations, times_matrix, label='Matrix rotation')
    plt.plot(iterations, times_quat, label='Quaternion rotation')
    plt.xlabel('Number of iterations')
    plt.ylabel('Execution time (s)')
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Performance comparison: Matrix vs Quaternion rotation')
    plt.legend()
    plt.grid(True)
    plt.show() 