import argparse
from img2chars.core import ImgToChars


def run_cli():
    parser = argparse.ArgumentParser(description="Конвертер изображений в ASCII-арт")
    parser.add_argument("path", help="Путь к изображению")
    parser.add_argument("-w", "--width", type=int, default=100, help="Ширина ASCII-арта")
    parser.add_argument("-m", "--mode", default="mono", choices=["mono", "color", "edges", "edges_cv", "smart_edges", "smart_edges_cv"], help="Режим рендеринга")
    parser.add_argument("-o", "--output", help="Файл для сохранения результата")

    args = parser.parse_args()

    try:
        converter = ImgToChars(mode=args.mode, width=args.width)
        result = converter.convert(args.path)
    except Exception as e:
        print(f"Ошибка: {e}")
        return

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        print(result)
