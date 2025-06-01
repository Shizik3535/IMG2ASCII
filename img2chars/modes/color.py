from PIL import Image
from .base import BaseRenderMode


class ColorMode(BaseRenderMode):
    def render(self, img: Image.Image, width: int) -> str:
        aspect_ratio = img.height / img.width
        height = int(aspect_ratio * width * 0.55)
        img = img.resize((width, height))
        img = img.convert("RGB")

        pixels = img.getdata()
        ascii_str = ""
        for i, pixel in enumerate(pixels):
            if i % width == 0 and i != 0:
                ascii_str += "\n"
            r, g, b = pixel
            brightness = int(0.299 * r + 0.587 * g + 0.114 * b)
            char = self.chars[brightness * (len(self.chars) - 1) // 255]
            ascii_str += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
        return ascii_str
