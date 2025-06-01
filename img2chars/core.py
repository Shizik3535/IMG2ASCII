from PIL import Image
from img2chars.modes import REGISTERED_MODES


class ImgToChars:
    def __init__(self, mode="mono", width=100, chars=None):
        if mode not in REGISTERED_MODES:
            raise ValueError(f"Неизвестный режим: {mode}")
        self.renderer = REGISTERED_MODES[mode](chars)
        self.width = width

    def convert(self, path: str) -> str:
        img = Image.open(path)
        return self.renderer.render(img, self.width)
