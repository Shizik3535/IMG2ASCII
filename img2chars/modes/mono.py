from PIL import Image
from .base import BaseRenderMode


class MonoMode(BaseRenderMode):
    def render(self, img: Image.Image, width: int) -> str:
        aspect_ratio = img.height / img.width
        height = int(aspect_ratio * width * 0.55)
        img = img.resize((width, height))
        img = img.convert("L")

        pixels = img.getdata()
        ascii_str = ""
        for i, pixel in enumerate(pixels):
            if i % width == 0 and i != 0:
                ascii_str += "\n"
            char = self.chars[pixel * (len(self.chars) - 1) // 255]
            ascii_str += char
        return ascii_str
