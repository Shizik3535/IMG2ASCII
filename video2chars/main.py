import sys
import os

sys.path.insert(0, os.path.abspath('../img2chars'))

from img2chars.modes import ColorMode
from video2chars import VideoAsciiPlayer


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py path_to_video [width] [fps]")
        return

    video_path = sys.argv[1]
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    fps = int(sys.argv[3]) if len(sys.argv) > 3 else 24

    mode = ColorMode()  # можно поменять на любой другой режим
    player = VideoAsciiPlayer(video_path, mode, width, fps)
    player.play()


if __name__ == '__main__':
    main()
