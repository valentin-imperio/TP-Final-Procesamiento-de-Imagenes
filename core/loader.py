import cv2


class ImageLoader:

    def load(self, image_path):

        image = cv2.imread(image_path)

        if image is None:
            raise FileNotFoundError(
                f"No se pudo cargar la imagen: {image_path}"
            )

        return image