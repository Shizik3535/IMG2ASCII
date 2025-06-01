import cv2
import os
import time
from PIL import Image


class WebcamAsciiPlayer:
    def __init__(self, render_mode, width=100, fps=24, cam_index=0):
        self.render_mode = render_mode
        self.width = width
        self.fps = fps
        self.cam_index = cam_index

    def play(self):
        cap = cv2.VideoCapture(self.cam_index)
        delay = 1 / self.fps

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Не удалось получить кадр с камеры")
                    break

                # BGR -> RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_img = Image.fromarray(frame_rgb)

                ascii_frame = self.render_mode.render(pil_img, self.width)

                os.system('cls' if os.name == 'nt' else 'clear')
                print(ascii_frame)

                time.sleep(delay)

        except KeyboardInterrupt:
            print("Остановка по запросу пользователя")

        finally:
            cap.release()


# Пример использования:
if __name__ == "__main__":
    from img2chars.modes.mono import MonoMode
    from img2chars.modes.color import ColorMode

    mode = ColorMode()
    player = WebcamAsciiPlayer(mode, width=120, fps=20)
    player.play()
