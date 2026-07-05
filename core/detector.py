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
    
    def sort_contours_by_area(self, contours):
        "Ordena los contornos desde el de mayor área al de menor."

        return sorted(
            contours,
            key=cv2.contourArea,
            reverse=True
        )


    def find_document_contour(self, contours):
        "Busca el primer contorno con cuatro vértices (Si detectan los cuatro vertices con mas area de la imagen encontramos la hoja)."

        sorted_contours = self.sort_contours_by_area(contours)

        for contour in sorted_contours:

            perimeter = cv2.arcLength(contour, True)

            approximation = cv2.approxPolyDP(
                contour,
                0.02 * perimeter,
                True
            )

            if len(approximation) == 4:
                return approximation

        return None