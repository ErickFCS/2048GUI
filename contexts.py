from config import *
import pygame as pg

class Rectangle:
    def __init__(self, width=20, height=20, xpos=0, ypos=0, anchor="center"):
        self.rect = pg.Rect(0, 0, width, height)
        self.place(xpos, ypos, anchor)

    def place(self, xpos, ypos, anchor="center"):
        ok = 0
        if anchor in ["topleft", "tl", "nw"]:
            self.rect.topleft = (xpos, ypos)
            ok = 1
        elif anchor in ["top", "t", "n"]:
            self.rect.top = (xpos, ypos)
            ok = 1
        elif anchor in ["topright", "tr", "ne"]:
            self.rect.topright = (xpos, ypos)
            ok = 1
        elif anchor in ["left", "l", "w"]:
            self.rect.left = (xpos, ypos)
            ok = 1
        elif anchor in ["center", "middle", "c", "m"]:
            self.rect.center = (xpos, ypos)
            ok = 1
        elif anchor in ["right", "r", "e"]:
            self.rect.right = (xpos, ypos)
            ok = 1
        elif anchor in ["bottomleft", "bl", "sw"]:
            self.rect.bottomleft = (xpos, ypos)
            ok = 1
        elif anchor in ["bottom", "b", "s"]:
            self.rect.bottomleft = (xpos, ypos)
            ok = 1
        elif anchor in ["bottomright", "br", "se"]:
            self.rect.bottomright = (xpos, ypos)
            ok = 1
        if ok == 1:
            self.xpos = xpos
            self.ypos = ypos
            self.anchor = anchor

    def move(self, x, y):
        self.place(self.xpos + x, self.ypos + y, self.anchor)

class Image(Rectangle):
    def __init__(self, src):
        super().__init__()
        self.image = pg.image.load(src)
        self.rect = self.image.get_rect()

def cStartUp(globs):
    globs.update({
            "image2":Image(IMAGE_2_SRC),
            "image4":Image(IMAGE_4_SRC),
            "image8":Image(IMAGE_8_SRC),
            "image16":Image(IMAGE_16_SRC),
            "image32":Image(IMAGE_32_SRC),
            "image64":Image(IMAGE_64_SRC),
            "image128":Image(IMAGE_128_SRC),
            "image256":Image(IMAGE_256_SRC),
            "image512":Image(IMAGE_512_SRC),
            "image1024":Image(IMAGE_1024_SRC),
            "image2048":Image(IMAGE_2048_SRC),
            "image4096":Image(IMAGE_4096_SRC),
            "image8192":Image(IMAGE_8192_SRC),
            "image16384":Image(IMAGE_16384_SRC),
            f"arial{TEXT_SIZE}Font":pg.font.Font(pg.font.match_font(TEXT_FONT), TEXT_SIZE)
    })
    
def cEnd(globs):
    text = globs[f"arial{TEXT_SIZE}Font"].render("You Lose!!!", True, TEXT_COLOR)
    textRect = text.get_rect()
    textRect.center = (WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2)
    globs["window"].blit(text, textRect)

def cGame(globs):
    globs["window"].fill(BACKGROUND_COLOR)
    for ii, iv in enumerate(globs["board"].cells):
        for vi, vv in enumerate(iv):
            if vv != 0:
                globs[f"image{vv}"].place(LEFT_MARGIN_BOARD + vi * IMAGES_WIDTH, TOP_MARGIN_BOARD + ii * IMAGES_HEIGHT, "tl")
                globs["window"].blit(globs[f"image{vv}"].image, globs[f"image{vv}"].rect)
    pg.draw.rect(globs["window"], BOARD_COLOR, Rectangle(265, 265, WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2), 5)
        
    