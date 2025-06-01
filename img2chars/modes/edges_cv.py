from PIL import Image
import numpy as np
import cv2
from .base import BaseRenderMode


class EdgesModeCV(BaseRenderMode):
    def __init__(self, chars=None):
        # Для контуров можно использовать один символ, например '#'
        super().__init__(chars=chars or "#")

    def render(self, img: Image.Image, width: int) -> str:
        aspect_ratio = img.height / img.width
        height = int(aspect_ratio * width * 0.55)
        img = img.resize((width, height))
        img = img.convert("L")

        img_np = np.array(img)

        edges = cv2.Canny(img_np, threshold1=100, threshold2=200)

        ascii_str = ""
        for y in range(edges.shape[0]):
            for x in range(edges.shape[1]):
                if edges[y, x] != 0:
                    ascii_str += self.chars[0]
                else:
                    ascii_str += " "
            ascii_str += "\n"

        return ascii_str
