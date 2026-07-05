from core.loader import ImageLoader
from core.enhancer import ImageEnhancer
from core.saver import ImageSaver


def main():

    loader = ImageLoader()
    enhancer = ImageEnhancer()
    saver = ImageSaver()

    image = loader.load("images/input/documento.jpg")

    gray_image = enhancer.to_grayscale(image)

    saver.save(
        gray_image,
        "images/output/grayscale.jpg"
    )

    print("Imagen guardada correctamente")


if __name__ == "__main__":
    main()