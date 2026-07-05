import cv2


class DocumentDetector:

    def detect_edges(self, image):
        " Detecta los bordes utilizando el algoritmo de Canny."
        return cv2.Canny(image, 75, 200)

    def find_contours(self, edges):
        "Busca todos los contornos presentes en la imagen, pero solo guarda los mas importantes."
        contours, _ = cv2.findContours(
            edges,
            cv2.RETR_LIST,
            cv2.CHAIN_APPROX_SIMPLE
            
        )

        return contours