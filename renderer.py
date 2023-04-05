import history
import logic
import constants

import numpy as np
import pygame as pg
import sys
import math

#Initialize the Board Matrix & Players
board = logic.createBoard()
logic.printBoard(board)
gameOver = False
turn = constants.p1

#Initialize PyGame
pg.init()

window = pg.display.set_mode(constants.windowSize)

#Render the board and all pieces
def renderBoard(board):
    #Create Normal Board
    for c in range(constants.colCount):
        for r in range(constants.rowCount):
            #pg.draw.rect(window, constants.BACKGROUND, (c*constants.SIZE, c*constants.SIZE, constants.SIZE, constants.SIZE))
            pg.draw.circle(window, constants.GRAY, (int(c*constants.SIZE + constants.SIZE/2), int(constants.rowCount * constants.SIZE -r*constants.SIZE) + constants.SIZE*3/2), constants.RADIUS)

    #Create Each Colored Coin in its Place
    for c in range(constants.colCount):
        for r in range(constants.rowCount):
            if board[r][c] == constants.p1:
                pg.draw.circle(window, constants.RED, (int(c*constants.SIZE + constants.SIZE/2), int(constants.rowCount * constants.SIZE -r*constants.SIZE) + constants.SIZE*3/2), constants.RADIUS)
            
            if board[r][c] == constants.p2:
                pg.draw.circle(window, constants.BLUE, (int(c*constants.SIZE + constants.SIZE/2), int(constants.rowCount * constants.SIZE -r*constants.SIZE) + constants.SIZE*3/2), constants.RADIUS)

    pg.display.update()

#Tentative on Time
#Render the Historical Games and Show the Outcome of each of those Games
def renderHistory():
    for i in range(len(history.history)):
        board = history.history[i]
        for c in range(constants.colCount):
            for r in range(constants.rowCount):
                pg.draw.rect(window, constants.BACKGROUND, (c*constants.HSIZE, c*constants.HSIZE, constants.HSIZE, constants.HSIZE))
                pg.draw.circle(window, constants.GRAY, (int(c*constants.HSIZE + constants.HSIZE/2), int(r*constants.HSIZE + constants.HSIZE/2)), constants.HRADIUS)

        for c in range(constants.colCount):
            for r in range(constants.rowCount):
                if board[r][c] == constants.p1:
                    pg.draw.circle(window, constants.RED, (int(c*constants.HSIZE + constants.HSIZE/2), int(r*constants.HSIZE + constants.HSIZE/2)), constants.HRADIUS)
                
                if board[r][c] == constants.p2:
                    pg.draw.circle(window, constants.BLUE, (int(c*constants.HSIZE + constants.HSIZE/2), int(r*constants.HSIZE + constants.HSIZE/2)), constants.HRADIUS)

#Blank Screen
def blank():
    pg.draw.rect(window, constants.BACKGROUND, (0,0,constants.width, constants.height))


#Input String, (x, y) coordinate for position, and size for display
def text(string, y, size, color):
    font = pg.font.SysFont("bahnscript", size)
    text = font.render(string, 1, color)

    text_rect = text.get_rect(center = (constants.width/2, y))
    window.blit(text, text_rect)
    pg.display.update()

def scoreboard(p1, p2):
    pg.draw.rect(window, constants.GRAY, (constants.SIZE*5/2,0,constants.SIZE*2,70))
    pg.draw.rect(window, constants.BACKGROUND, (constants.SIZE*5/2 + 2,0,constants.SIZE*2 - 4,68))
    text(str(p1) + "     " + str(p2), 30, 50, constants.WHITE)

