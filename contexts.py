from config import *
import pygame as pg
import mysql.connector


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
    globs.update(
        {
            "image2": Image(IMAGE_2_SRC),
            "image4": Image(IMAGE_4_SRC),
            "image8": Image(IMAGE_8_SRC),
            "image16": Image(IMAGE_16_SRC),
            "image32": Image(IMAGE_32_SRC),
            "image64": Image(IMAGE_64_SRC),
            "image128": Image(IMAGE_128_SRC),
            "image256": Image(IMAGE_256_SRC),
            "image512": Image(IMAGE_512_SRC),
            "image1024": Image(IMAGE_1024_SRC),
            "image2048": Image(IMAGE_2048_SRC),
            "image4096": Image(IMAGE_4096_SRC),
            "image8192": Image(IMAGE_8192_SRC),
            "image16384": Image(IMAGE_16384_SRC),
            f"arial{TEXT_SIZE}Font": pg.font.Font(
                pg.font.match_font(TEXT_FONT), TEXT_SIZE
            ),
        }
    )


def cEnd(globs):
    mydb = mysql.connector.connect(host="localhost", user="root", password="csef#2006")
    mycursor = mydb.cursor()
    mycursor.execute("use minecraft2048")
    
    
    
    mycursor.execute("select * from score ORDER BY puntaje DESC limit 3")
    playerList = list(mycursor)
    player1text = f"{playerList[0][1]}: {playerList[0][2]}"
    player2text = f"{playerList[1][1]}: {playerList[1][2]}"
    player3text = f"{playerList[2][1]}: {playerList[2][2]}"
    text = globs[f"arial{TEXT_SIZE}Font"].render("You Lose!!!", True, TEXT_COLOR)
    player1 = globs[f"arial{TEXT_SIZE}Font"].render(player1text, True, TEXT_COLOR)
    player2 = globs[f"arial{TEXT_SIZE}Font"].render(player2text, True, TEXT_COLOR)
    player3 = globs[f"arial{TEXT_SIZE}Font"].render(player3text, True, TEXT_COLOR)
    textRect = text.get_rect()
    player1Rect = player1.get_rect()
    player2Rect = player2.get_rect()
    player3Rect = player3.get_rect()
    textRect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 - TEXT_SIZE)
    player1Rect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
    player2Rect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + TEXT_SIZE)
    player3Rect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 2 * TEXT_SIZE)
    globs["window"].blit(text, textRect)
    globs["window"].blit(player1, player1Rect)
    globs["window"].blit(player2, player2Rect)
    globs["window"].blit(player3, player3Rect)


def cGame(globs):
    globs["window"].fill(BACKGROUND_COLOR)
    for ii, iv in enumerate(globs["board"].cells):
        for vi, vv in enumerate(iv):
            if vv != 0:
                globs[f"image{vv}"].place(
                    LEFT_MARGIN_BOARD + vi * IMAGES_WIDTH,
                    TOP_MARGIN_BOARD + ii * IMAGES_HEIGHT,
                    "tl",
                )
                globs["window"].blit(
                    globs[f"image{vv}"].image, globs[f"image{vv}"].rect
                )
    pg.draw.rect(
        globs["window"],
        BOARD_COLOR,
        Rectangle(265, 265, WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2),
        5,
    )
