from os import system
from random import randint

class Board:
    def __init__(self, size):
        self.size = size
        self.loser = False
        self.cells = [[0 for v in range(size[1])] for i in range(size[0])]
        self.addNum()
    def move(self, direction):
        if direction == 0:      #left
            self.add(self.cells)
        elif direction == 1:    #up
            cellsUp = [[None for v in range(self.size[0])] for i in range(self.size[1])]
            ii = 0
            for i in self.cells:
                vi = self.size[1] - 1
                for v in i:
                    cellsUp[vi][ii] = v
                    vi -= 1
                ii += 1
            self.add(cellsUp)
            ii = self.size[1] - 1
            for i in cellsUp:
                vi = 0
                for v in i:
                    self.cells[vi][ii] = v
                    vi += 1
                ii -= 1
        elif direction == 2:    #down
            cellsDown = [[None for i in range(self.size[0])] for v in range(self.size[1])]
            ii = self.size[0] - 1
            for i in self.cells:
                vi = 0
                for v in i:
                    cellsDown[vi][ii] = v
                    vi += 1
                ii -= 1
            self.add(cellsDown)
            ii = 0
            for i in cellsDown:
                vi = self.size[0] - 1
                for v in i:
                    self.cells[vi][ii] = v
                    vi -= 1
                ii += 1
        elif direction == 3:    #right
            cellsRight = [[None for i in range(self.size[1])] for v in range(self.size[0])]
            ii = 0
            for i in self.cells:
                vi = self.size[1] - 1
                for v in i:
                    cellsRight[ii][vi] = v
                    vi -= 1
                ii += 1
            self.add(cellsRight)
            ii = 0
            for i in cellsRight:
                vi = self.size[1] - 1
                for v in i:
                    self.cells[ii][vi] = v
                    vi -= 1
                ii += 1
    def addNum(self):
        try:
            emptyI = []
            for ii, iv in enumerate(self.cells):
                for vi, vv in enumerate(iv):
                    if vv == 0:
                        emptyI.append((ii, vi))
            i = randint(0, len(emptyI)-1)
            self.cells[emptyI[i][0]][emptyI[i][1]] = 2
        except:
            self.loser = True
    def add(self, cells):
        i = 0
        while i < len(cells):
            v = 0
            prev = None
            previ = None
            while v < len(cells[0]):
                if cells[i][v] == prev:
                    cells[i][previ] = prev * 2
                    cells[i][v] = 0
                    prev *= 2
                    # prev = None
                    # previ = None
                    # v = 0
                    # continue
                elif cells[i][v] != 0:
                    prev = cells[i][v]
                    previ = v
                v += 1
            i += 1
        i = 0
        while i < len(cells):
            v = 0
            j = 0
            while v < len(cells[0]):
                if cells[i][v] != 0:
                    cells[i][j] = cells[i][v]
                    if v != j:
                        cells[i][v] = 0 
                    j += 1
                v += 1
            i += 1
    def restart(self):
        self.cells = [[0 for v in range(self.size[1])] for i in range(self.size[0])]
        self.loser = False
        self.addNum()
    
if __name__ == "__main__":
    def printBoard(board):
        print("------------------------", end="\n")
        # print("", end="\n")
        for i in board.cells:
            print("|  ", end="")
            for v in i:
                print(v, end="  |  ")
            print("\n------------------------", end="\n")
            # print("\n", end="\n")
    a = Board((4, 4))
    while True:
        system("cls")
        a.addNum()
        printBoard(a)
        if a.loser:
            print("You Lose!!!")
            system("pause > nul")
            break
        else:
            inp = input("Enter w/a/s/d: ")
            if inp == "w":
                a.move(1)
            elif inp == "a":
                a.move(0)
            elif inp == "s":
                a.move(2)
            elif inp == "d":
                a.move(3)