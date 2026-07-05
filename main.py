from core.scanner import DocumentScanner


def main():

    scanner = DocumentScanner()

    scanner.scan(
        input_path="images/input/documento.jpg",
        output_path="images/output/blur.jpg"
    )

    print("Imagen procesada correctamente")


if __name__ == "__main__":
    main()