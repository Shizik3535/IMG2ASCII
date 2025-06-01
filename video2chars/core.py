import cv2
import os
import time
from PIL import Image


class VideoAsciiPlayer:
    def __init__(self, video_path, render_mode, width=100, fps=5):
        self.video_path = video_path
        self.render_mode = render_mode
        self.width = width
        self.fps = fps

    def play(self):
        cap = cv2.VideoCapture(self.video_path)
        delay = 1 / self.fps

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_img = Image.fromarray(frame_rgb)

                ascii_frame = self.render_mode.render(pil_img, self.width)

                os.system('cls' if os.name == 'nt' else 'clear')
                print(ascii_frame)
                time.sleep(delay)

        finally:
            cap.release()
