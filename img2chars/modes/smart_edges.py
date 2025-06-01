from PIL import Image
from .base import BaseRenderMode


class SmartEdgesMode(BaseRenderMode):
    def __init__(self, chars=None, threshold=30):
        # chars не используем, потому что символы определяются динамически
        super().__init__(chars=None)
        self.threshold = threshold

    def _is_edge(self, pixels, x, y, width, height):
        center = pixels[x, y]
        left = pixels[x - 1, y] if x > 0 else center
        right = pixels[x + 1, y] if x < width - 1 else center
        up = pixels[x, y - 1] if y > 0 else center
        down = pixels[x, y + 1] if y < height - 1 else center

        dx = abs(right - left)
        dy = abs(down - up)

        edge_strength = dx + dy
        return edge_strength > self.threshold

    def choose_char(self, edges_map, x, y, width, height):
        # Проверяем соседей — есть ли граница сверху, снизу, слева, справа
        def has_edge(xx, yy):
            if 0 <= xx < width and 0 <= yy < height:
                return edges_map[yy][xx]
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
        # Один сосед
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

        pixels = img.load()

        edges_map = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(self._is_edge(pixels, x, y, width, height))
            edges_map.append(row)

        ascii_str = ""
        for y in range(height):
            for x in range(width):
                if edges_map[y][x]:
                    ascii_str += self.choose_char(edges_map, x, y, width, height)
                else:
                    ascii_str += " "
            ascii_str += "\n"

        return ascii_str
