
import cv2
import numpy as np


class PerspectiveTransformer:

    "Se ordenan los cuatro puntos del documento"
    def order_points(self, points):

        points = points.reshape(4, 2)

        ordered = np.zeros((4, 2), dtype="float32")

        sums = points.sum(axis=1)

        ordered[0] = points[np.argmin(sums)]
        ordered[2] = points[np.argmax(sums)]

        differences = np.diff(points, axis=1)

        ordered[1] = points[np.argmin(differences)]
        ordered[3] = points[np.argmax(differences)]

        return ordered

    "Calcula el ancho y el alto del documento."
    def calculate_dimensions(self, points):

     

        (top_left, top_right, bottom_right, bottom_left) = points

        width_top = np.linalg.norm(top_right - top_left)
        width_bottom = np.linalg.norm(bottom_right - bottom_left)

        max_width = max(int(width_top), int(width_bottom))

        height_left = np.linalg.norm(bottom_left - top_left)
        height_right = np.linalg.norm(bottom_right - top_right)

        max_height = max(int(height_left), int(height_right))

        return max_width, max_height


    def destination_points(self, width, height):
        "Devuelve los puntos de destino para la transformación de perspectiva."
        return np.array([
            [0, 0],
            [width - 1, 0],
            [width - 1, height - 1],
            [0, height - 1]
        ], dtype="float32")