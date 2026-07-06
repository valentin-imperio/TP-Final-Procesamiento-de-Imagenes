import cv2


class DocumentDetector:

    def detect_edges(self, image):
        #Detecta los bordes de la imagen utilizando el algoritmo de Canny

        return cv2.Canny(image, 75, 200)

    def find_contours(self, edges):
        #Busca todos los contornos presentes en la imagen, pero solo guarda los mas importantes

        contours, _ = cv2.findContours(
            edges,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
            
        )

        return contours
    
    def sort_contours_by_area(self, contours):
        #Ordena los contornos desde el de mayor área al de menor

        return sorted(
            contours,
            key=cv2.contourArea,
            reverse=True
        )


    def find_document_contour(self, contours):

        sorted_contours = self.sort_contours_by_area(contours)

        for contour in sorted_contours:

            area = cv2.contourArea(contour)
            #Solo queremos contornos grandes
            if area < 5000:
                continue
            perimeter = cv2.arcLength(contour, True)

            approximation = cv2.approxPolyDP(
                contour,
                0.02 * perimeter,
                True
            )

            # S tiene 4 vértices, asumimos que es el documento
            if len(approximation) == 4:
                return approximation

        return None
    
    def draw_contour(self, image, contour):
       
        #Dibuja el contorno del documento sobre la imagen

        image_copy = image.copy()

        cv2.drawContours(
            image_copy,
            [contour],
            -1,
            (0, 255, 0),
            3
        )

        return image_copy