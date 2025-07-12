import numpy as np

#rotation_matrices_for_x_y_z_axes
def rotation_x(theta):
    """#matrice_rotation_autour_axe_x
    Retourne la matrice de rotation autour de l'axe X d'un angle theta (en radians).
    """
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [1, 0, 0],
        [0, c, -s],
        [0, s, c]
    ])


def rotation_y(theta):
    """#matrice_rotation_autour_axe_y
    Retourne la matrice de rotation autour de l'axe Y d'un angle theta (en radians).
    """
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [c, 0, s],
        [0, 1, 0],
        [-s, 0, c]
    ])


def rotation_z(theta):
    """#matrice_rotation_autour_axe_z
    Retourne la matrice de rotation autour de l'axe Z d'un angle theta (en radians).
    """
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [c, -s, 0],
        [s, c, 0],
        [0, 0, 1]
    ])


def rotation_arbitrary_axis(axis, theta):
    """#rotation_autour_axe_quelconque_avec_matrice_passage
    Retourne la matrice de rotation autour d'un axe arbitraire (vecteur unitaire) d'un angle theta.
    """
    axis = np.asarray(axis)
    axis = axis / np.linalg.norm(axis)
    x, y, z = axis
    c = np.cos(theta)
    s = np.sin(theta)
    C = 1 - c
    return np.array([
        [c + x*x*C, x*y*C - z*s, x*z*C + y*s],
        [y*x*C + z*s, c + y*y*C, y*z*C - x*s],
        [z*x*C - y*s, z*y*C + x*s, c + z*z*C]
    ])


def rotate_vector_matrix(vector, rotation_matrix):
    """#application_rotation_sur_vecteur
    Applique la matrice de rotation à un vecteur 3D.
    """
    return np.dot(rotation_matrix, vector) 