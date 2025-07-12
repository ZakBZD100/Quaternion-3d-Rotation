import numpy as np
import pytest
from src.matrix_rotation import rotation_x, rotate_vector_matrix
from src.quaternion_rotation import Quaternion, quaternion_from_axis_angle, rotate_vector_quaternion

#test_matrice_identite
def test_matrix_rotation_identity():
    v = np.array([1, 2, 3])
    I = np.eye(3)
    v_rot = rotate_vector_matrix(v, I)
    assert np.allclose(v, v_rot)

#test_produit_quaternions
def test_quaternion_multiplication():
    q1 = Quaternion(1, 0, 1, 0)
    q2 = Quaternion(1, 0.5, 0.5, 0.75)
    q_prod = q1.multiply(q2)
    # Produit manuel pour vérification
    expected = Quaternion(0.5, 1.25, 1.5, 0.25)
    assert np.allclose([q_prod.w, q_prod.x, q_prod.y, q_prod.z], [expected.w, expected.x, expected.y, expected.z])

#test_equivalence_methodes_rotation
def test_rotation_equivalence():
    v = np.array([1, 0, 0])
    theta = np.pi / 2
    Rz = rotation_x(theta)
    v_rot_matrix = rotate_vector_matrix(v, Rz)
    qx = quaternion_from_axis_angle([1, 0, 0], theta)
    v_rot_quat = rotate_vector_quaternion(v, qx)
    assert np.allclose(v_rot_matrix, v_rot_quat) 