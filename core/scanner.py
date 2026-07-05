from core.loader import ImageLoader
from core.enhancer import ImageEnhancer
from core.saver import ImageSaver


class DocumentScanner:

    def __init__(self):
        self.loader = ImageLoader()
        self.enhancer = ImageEnhancer()
        self.saver = ImageSaver()

    def scan(self, input_path, output_path):

        image = self.loader.load(input_path)

        gray_image = self.enhancer.to_grayscale(image)

        blur_image = self.enhancer.gaussian_blur(gray_image)

        self.saver.save(
            blur_image,
            output_path
        )

        return blur_image