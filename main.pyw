import pygame as pg

from config import *
from events import *
from contexts import *
from board import Board

pg.init()
clock = pg.time.Clock()
pg.display.set_caption(CAPTION)
pg.display.set_icon(pg.image.load(ICON_IMAGE_SRC))
window = pg.display.set_mode(WINDOW_SIZE)

board = Board((4, 4))

user_text = ""
finished = 0
context = 1

cStartUp(globals())

loop = True
while loop:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            eQuit(globals())
            break
        elif event.type == pg.KEYDOWN and context == 1:
            if event.key in [119, 1073741906]:  # w
                eUp(globals())
            elif event.key in [97, 1073741904]:  # a
                eLeft(globals())
            elif event.key in [115, 1073741905]:  # s
                eDown(globals())
            elif event.key in [100, 1073741903]:  # d
                eRight(globals())
            elif event.key in [114]:  # r
                eRestart(globals())
        elif event.type == pg.KEYDOWN and context == 0:
            if event.key == pg.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pg.K_RETURN:
                finished = 1
                cEnd(globals())
                eRestart(globals())
                finished = 0
            else:
                if len(user_text) < 8:
                    user_text += event.unicode

    if context == 0:
        cEnd(globals())
    elif context == 1:
        cGame(globals())

    pg.display.update()
    clock.tick(FPS)
pg.quit()
