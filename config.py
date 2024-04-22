import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

CAPTION = "2048"
ICON_IMAGE_SRC = resource_path("./sprites/block2048.png")
IMAGE_2_SRC = resource_path("./sprites/block2.png")
IMAGE_4_SRC = resource_path("./sprites/block4.png")
IMAGE_8_SRC = resource_path("./sprites/block8.png")
IMAGE_16_SRC = resource_path("./sprites/block16.png")
IMAGE_32_SRC = resource_path("./sprites/block32.png")
IMAGE_64_SRC = resource_path("./sprites/block64.png")
IMAGE_128_SRC = resource_path("./sprites/block128.png")
IMAGE_256_SRC = resource_path("./sprites/block256.png")
IMAGE_512_SRC = resource_path("./sprites/block512.png")
IMAGE_1024_SRC = resource_path("./sprites/block1024.png")
IMAGE_2048_SRC = resource_path("./sprites/block2048.png")
IMAGE_4096_SRC = resource_path("./sprites/block4096.png")
IMAGE_8192_SRC = resource_path("./sprites/block8192.png")
IMAGE_16384_SRC = resource_path("./sprites/block16384.png")
FPS = 30
WINDOW_SIZE = (356, 356)
BACKGROUND_COLOR = "#dddddd"
BOARD_COLOR = "#eeeeee"
TEXT_COLOR = "#ff0000"
TEXT_SIZE = 64
TEXT_FONT = "Arial"
TOP_MARGIN_BOARD = 50
LEFT_MARGIN_BOARD = 50
IMAGES_WIDTH = 64
IMAGES_HEIGHT = 64