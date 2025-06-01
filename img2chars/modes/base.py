from abc import ABC, abstractmethod
from PIL import Image


class BaseRenderMode(ABC):
    def __init__(self, chars=None):
        self.chars = chars or "@%#*+=-:. "

    @abstractmethod
    def render(self, img: Image.Image, width: int) -> str:
        """Возвращает ASCII-арт в виде строки"""
        pass
