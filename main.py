from core.loader import ImageLoader


loader = ImageLoader()

image = loader.load("images/input/documento.jpg")

print(image.shape)