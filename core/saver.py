import cv2


class ImageSaver:

    def save(self, image, output_path):
        success = cv2.imwrite(output_path, image)

        if not success:
            raise IOError(
                f"No se pudo guardar la imagen en: {output_path}"
            )