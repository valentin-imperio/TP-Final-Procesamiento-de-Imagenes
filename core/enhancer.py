import cv2
import numpy as np

class ImageEnhancer:

    def to_grayscale(self, image):
        "Convierte una imagen color a escala de grises."
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    def gaussian_blur(self, image):
        "Reduce el ruido mediante un filtro Gaussiano."
        return cv2.GaussianBlur(image, (5, 5), 0)
    
    def adaptive_threshold(self, image):
        "Convierte la imagen en blanco y negro adaptativo."

        return cv2.adaptiveThreshold(
            image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )
    
    def close_edges(self, image):
            """
            Une pequeños cortes en los bordes mediante operaciones morfológicas.
            """

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
        """
        Redimensiona la imagen manteniendo la relación de aspecto.
        Devuelve la imagen redimensionada y el factor de escala.
        """

        ratio = image.shape[0] / height

        width = int(image.shape[1] / ratio)

        resized = cv2.resize(
            image,
            (width, height)
        )

        return resized, ratio
    
    def clahe(self, image):
        """
        Mejora el contraste local de una imagen en escala de grises.
        """

        clahe = cv2.createCLAHE(
            clipLimit=2.0,
            tileGridSize=(8, 8)
        )

        return clahe.apply(image)
    
    def sharpen(self, image):
        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ], dtype=np.float32)

        return cv2.filter2D(image, -1, kernel)