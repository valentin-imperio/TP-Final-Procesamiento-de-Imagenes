import cv2


class DocumentDetector:

    def detect_edges(self, image):
        """
        Detecta los bordes utilizando el algoritmo de Canny.
        """

        return cv2.Canny(
            image,
            threshold1=75,
            threshold2=200
        )