from core.loader import ImageLoader
from core.enhancer import ImageEnhancer
from core.saver import ImageSaver
from core.detector import DocumentDetector
from core.transformer import PerspectiveTransformer

import numpy as np


class DocumentScanner:

    def __init__(self):
        self.loader = ImageLoader()
        self.enhancer = ImageEnhancer()
        self.detector = DocumentDetector()
        self.transformer = PerspectiveTransformer()
        self.saver = ImageSaver()

    def scan(self, input_path, output_path):

        image = self.loader.load(input_path)

        resized_image, ratio = self.enhancer.resize(image)

        gray_image = self.enhancer.to_grayscale(resized_image)

        blur_image = self.enhancer.gaussian_blur(gray_image)

        edges = self.detector.detect_edges(blur_image)

        edges = self.enhancer.close_edges(edges)

        contours = self.detector.find_contours(edges)

        document_contour = self.detector.find_document_contour(contours)

        if document_contour is None:
            raise ValueError("No se encontró ningún documento en la imagen.")

        print("Documento detectado correctamente.")

        # ===== Escalar el contorno nuevamente al tamaño original =====
        document_contour = document_contour.reshape(4, 2)
        document_contour = document_contour * ratio
        document_contour = document_contour.astype(np.float32)

        # Warp utilizando la imagen ORIGINAL
        warped_image = self.transformer.warp(
            image,
            document_contour
        )

        # Convertir el documento corregido a escala de grises
        gray_warped = self.enhancer.to_grayscale(
            warped_image
        )

        contrast_image = self.enhancer.clahe(
            gray_warped
        )

        final_image = self.enhancer.sharpen(
            contrast_image
        )

        self.saver.save(
            final_image,
            output_path
        )

        return final_image