import cv2
import numpy as np


class ImageEnhancer:

    def to_grayscale(self, image):
        # Pasa la imagen a escala de grises
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def gaussian_blur(self, image):
        # Reduce el ruido de la imagen.
        return cv2.GaussianBlur(image, (5, 5), 0)

    def adaptive_threshold(self, image):
        # Convierte la imagen a blanco y negro utilizando un umbral adaptativo
        return cv2.adaptiveThreshold(
            image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

    def close_edges(self, image):
        # Une  cortes pequeños para que detecte mejor la hojas

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (5, 5)
        )

        image = cv2.dilate(
            image,
            kernel,
            iterations=2
        )

        image = cv2.erode(
            image,
            kernel,
            iterations=1
        )

        return image

    def resize(self, image, height=500):
        # Redimensiona la imagen

        ratio = image.shape[0] / height
        width = int(image.shape[1] / ratio)

        resized = cv2.resize(
            image,
            (width, height)
        )

        return resized, ratio

    def clahe(self, image):
        # Mejora el contraste local de la imagen

        clahe = cv2.createCLAHE(
            clipLimit=2.0,
            tileGridSize=(8, 8)
        )

        return clahe.apply(image)

    def sharpen(self, image):
        # Aplica un filtro de nitidez a la imagen

        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ], dtype=np.float32)

        return cv2.filter2D(image, -1, kernel)