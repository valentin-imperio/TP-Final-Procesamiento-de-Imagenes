from core.loader import ImageLoader
from core.enhancer import ImageEnhancer
from core.saver import ImageSaver
from core.detector import DocumentDetector

class DocumentScanner:

    def __init__(self):
        self.loader = ImageLoader()
        self.enhancer = ImageEnhancer()
        self.detector = DocumentDetector()
        self.saver = ImageSaver()

    def scan(self, input_path, output_path):

        image = self.loader.load(input_path)

        gray_image = self.enhancer.to_grayscale(image)

        blur_image = self.enhancer.gaussian_blur(gray_image)

        edges = self.detector.detect_edges(blur_image)

        self.saver.save(
            edges,
            output_path
        )

        return edges