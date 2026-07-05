import cv2


class ImageEnhancer:

    def to_grayscale(self, image):
        "Convierte una imagen color a escala de grises."
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    def gaussian_blur(self, image):
        """Reduce el ruido mediante un filtro Gaussiano."""
        return cv2.GaussianBlur(image, (5, 5), 0)