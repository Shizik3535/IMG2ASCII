from PIL import Image
import numpy as np
import cv2
from .base import BaseRenderMode


class SmartEdgesModeCV(BaseRenderMode):
    def __init__(self, chars=None, threshold1=100, threshold2=200):
        super().__init__(chars=None)
        self.threshold1 = threshold1
        self.threshold2 = threshold2

    def choose_char(self, edges_map, x, y, width, height):
        def has_edge(xx, yy):
            if 0 <= xx < width and 0 <= yy < height:
                return edges_map[yy, xx] > 0
            return False

        top = has_edge(x, y - 1)
        bottom = has_edge(x, y + 1)
        left = has_edge(x - 1, y)
        right = has_edge(x + 1, y)

        if top and bottom and not left and not right:
            return '│'
        if left and right and not top and not bottom:
            return '─'
        if bottom and right and not top and not left:
            return '┌'
        if bottom and left and not top and not right:
            return '┐'
        if top and right and not bottom and not left:
            return '└'
        if top and left and not bottom and not right:
            return '┘'
        if left and right and top and not bottom:
            return '┴'
        if left and right and bottom and not top:
            return '┬'
        if top and bottom and right and not left:
            return '├'
        if top and bottom and left and not right:
            return '┤'
        if top and bottom and left and right:
            return '┼'
        if top or bottom:
            return '│'
        if left or right:
            return '─'
        return '·'

    def render(self, img: Image.Image, width: int) -> str:
        aspect_ratio = img.height / img.width
        height = int(aspect_ratio * width * 0.55)

        img = img.resize((width, height))
        img = img.convert("L")

        img_np = np.array(img)

        edges = cv2.Canny(img_np, self.threshold1, self.threshold2)

        ascii_str = ""
        for y in range(height):
            for x in range(width):
                if edges[y, x] != 0:
                    ascii_str += self.choose_char(edges, x, y, width, height)
                else:
                    ascii_str += " "
            ascii_str += "\n"

        return ascii_str
