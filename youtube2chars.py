import os
import subprocess
import cv2
import sys
import time
from PIL import Image
from img2chars.modes.color import ColorMode  # Или другой режим

TEMP_VIDEO_FILE = "temp_video.mp4"
COOKIES_FILE = "cookies.txt"


def download_youtube_video(url, filename):
    print("Скачивание видео...")

    cmd = [
        "yt-dlp",
        "--cookies", COOKIES_FILE,
        "-f", "mp4",
        "-o", filename,
        url
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("Ошибка при скачивании видео:")
        print(result.stderr)
        raise RuntimeError("Не удалось скачать видео")


def play_video_ascii(path: str, render_mode, width=100, fps_limit=30):
    cap = cv2.VideoCapture(path)
    delay = 1 / fps_limit

    print("\x1b[2J", end="")  # Очистка экрана

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(frame_rgb)
            ascii_frame = render_mode.render(pil_img, width)

            sys.stdout.write("\x1b[H")
            sys.stdout.write(ascii_frame)
            sys.stdout.flush()

            time.sleep(delay)
    finally:
        cap.release()
        print("\nЗавершено.")


if __name__ == "__main__":
    url = input("Введите URL YouTube-видео: ").strip()
    download_youtube_video(url, TEMP_VIDEO_FILE)

    mode = ColorMode()  # или другой
    play_video_ascii(TEMP_VIDEO_FILE, mode, width=100, fps_limit=15)

    os.remove(TEMP_VIDEO_FILE)
