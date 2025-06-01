from PIL import Image
from .base import BaseRenderMode


class EdgesMode(BaseRenderMode):
    def __init__(self, chars=None):
        super().__init__(chars=chars or "#")

    def render(self, img: Image.Image, width: int) -> str:
        aspect_ratio = img.height / img.width
        height = int(aspect_ratio * width * 0.55)
        img = img.resize((width, height))
        img = img.convert("L")

        pixels = img.load()

        ascii_str = ""
        for y in range(height):
            for x in range(width):
                center = pixels[x, y]

                left = pixels[x - 1, y] if x > 0 else center
                right = pixels[x + 1, y] if x < width - 1 else center
                up = pixels[x, y - 1] if y > 0 else center
                down = pixels[x, y + 1] if y < height - 1 else center

                dx = abs(right - left)
                dy = abs(down - up)

                edge_strength = dx + dy

                threshold = 30
                if edge_strength > threshold:
                    ascii_str += self.chars[0]
                else:
                    ascii_str += " "
            ascii_str += "\n"

        return ascii_str
