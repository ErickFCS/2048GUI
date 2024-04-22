from config import *

def eQuit(globs):
    globs.update({"loop":False})

def eUp(globs):       #w
    globs["board"].move(1)
    globs["board"].addNum()
    if globs["board"].loser:
        globs["context"] = 0

def eLeft(globs):     #a
    globs["board"].move(0)
    globs["board"].addNum()
    if globs["board"].loser:
        globs["context"] = 0

def eDown(globs):     #s
    globs["board"].move(2)
    globs["board"].addNum()
    if globs["board"].loser:
        globs["context"] = 0

def eRight(globs):    #d
    globs["board"].move(3)
    globs["board"].addNum()
    if globs["board"].loser:
        globs["context"] = 0

def eRestart(globs):  #r
    globs["board"].restart()
    globs["context"] = 1