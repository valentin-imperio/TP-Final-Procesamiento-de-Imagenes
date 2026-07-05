import cv2


class DocumentDetector:

    def detect_edges(self, image):
        " Detecta los bordes utilizando el algoritmo de Canny."

        return cv2.Canny(image, 75, 200)

    def find_contours(self, edges):
        "Busca todos los contornos presentes en la imagen, pero solo guarda los mas importantes."

        contours, _ = cv2.findContours(
            edges,
            cv2.RETR_EXTERNAL,
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

        sorted_contours = self.sort_contours_by_area(contours)

        for i, contour in enumerate(sorted_contours):

            area = cv2.contourArea(contour)
            if area < 5000:
                continue
            perimeter = cv2.arcLength(contour, True)

            approximation = cv2.approxPolyDP(
                contour,
                0.02 * perimeter,
                True
            )

            
            if len(approximation) == 4:
                print("Documento encontrado")
                return approximation


            # Dibujar este contorno para inspeccionarlo
            preview = self.draw_contour(
                cv2.imread("images/input/documento.jpg"),
                approximation
            )

            cv2.imwrite(
                f"images/output/debug_contour_{i+1}.jpg",
                preview
            )

        return None
    
    def draw_contour(self, image, contour):
        """
        Dibuja el contorno detectado sobre una copia de la imagen.
        """

        image_copy = image.copy()

        cv2.drawContours(
            image_copy,
            [contour],
            -1,
            (0, 255, 0),
            3
        )

        return image_copy