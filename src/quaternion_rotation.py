import numpy as np

class Quaternion:
    def __init__(self, w, x, y, z):
        """#quaternion_w_x_y_z_components
        Initialise un quaternion avec les composantes w, x, y, z.
        """
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def multiply(self, other):
        """#produit_quaternions_16_mult_8_add
        Multiplie ce quaternion par un autre quaternion.
        """
        w1, x1, y1, z1 = self.w, self.x, self.y, self.z
        w2, x2, y2, z2 = other.w, other.x, other.y, other.z
        w = w1*w2 - x1*x2 - y1*y2 - z1*z2
        x = w1*x2 + x1*w2 + y1*z2 - z1*y2
        y = w1*y2 - x1*z2 + y1*w2 + z1*x2
        z = w1*z2 + x1*y2 - y1*x2 + z1*w2
        return Quaternion(w, x, y, z)

    def conjugate(self):
        """#conjugue_quaternion
        Retourne le conjugué du quaternion.
        """
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def inverse(self):
        """#inverse_quaternion
        Retourne l'inverse du quaternion.
        """
        norm_sq = self.w**2 + self.x**2 + self.y**2 + self.z**2
        conj = self.conjugate()
        return Quaternion(conj.w / norm_sq, conj.x / norm_sq, conj.y / norm_sq, conj.z / norm_sq)

    def normalize(self):
        """#normalisation_quaternion_unitaire
        Normalise le quaternion pour qu'il soit unitaire.
        """
        norm = np.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)
        self.w /= norm
        self.x /= norm
        self.y /= norm
        self.z /= norm
        return self

def quaternion_from_axis_angle(axis, theta):
    """#quaternion_depuis_axe_angle_cos_theta_2_sin_theta_2
    Crée un quaternion à partir d'un axe (vecteur unitaire) et d'un angle theta.
    """
    axis = np.asarray(axis)
    axis = axis / np.linalg.norm(axis)
    w = np.cos(theta / 2)
    x, y, z = axis * np.sin(theta / 2)
    return Quaternion(w, x, y, z)

def rotate_vector_quaternion(vector, quaternion):
    """#rotation_vecteur_q_v_q_inverse_48_mult_24_add
    Applique la rotation définie par le quaternion à un vecteur 3D.
    """
    q = quaternion
    v = Quaternion(0, *vector)
    q_inv = q.inverse()
    v_rot = q.multiply(v).multiply(q_inv)
    return np.array([v_rot.x, v_rot.y, v_rot.z]) 