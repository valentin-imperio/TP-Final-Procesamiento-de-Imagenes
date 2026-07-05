from pathlib import Path
from core.scanner import DocumentScanner


def main():

    scanner = DocumentScanner()

    input_folder = Path("images/input")
    output_folder = Path("images/output")

    output_folder.mkdir(exist_ok=True)

    extensions = [".jpg", ".jpeg", ".png", ".bmp"]

    for image_path in input_folder.iterdir():

        if image_path.suffix.lower() not in extensions:
            continue

        output_path = output_folder / f"scanned_{image_path.name}"

        print(f"Procesando: {image_path.name}")

        try:
            scanner.scan(
                str(image_path),
                str(output_path)
            )

            print("OK\n")

        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()