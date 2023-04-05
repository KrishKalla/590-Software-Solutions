import numpy as np
import pygame as pg
import keyboard
import sys
import math
import board

import pynput as input

RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (10,10,10)
GRAY = (150, 150, 150)

mouseListener = input.mouse.Listener(suppress=True)

def renderBoard(BOARD):
    for c in range(board.columnCount):
        for r in range (board.rowCount):
            pg.draw.rect(window, BLACK, (c*SIZE,r*SIZE + SIZE, SIZE, SIZE))
            pg.draw.circle(window, GRAY, (int(c*SIZE+SIZE/2), int(r*SIZE+SIZE+SIZE/2)), RADIUS)

    for c in range(board.columnCount):
        for r in range(board.rowCount):
            if BOARD[r][c] == board.p1:
                pg.draw.circle(window, RED, (int(c*SIZE+SIZE/2), int(height - r*SIZE-SIZE/2)), RADIUS)
            if BOARD[r][c] == board.p2:
                pg.draw.circle(window, BLUE, (int(c*SIZE+SIZE/2), int(height - r*SIZE-SIZE/2)), RADIUS)
    
    pg.display.update()



def renderHistory():
    # for i in range(len(board.history)):
    #     for c in range(board.columnCount):
    #         for r in range (board.rowCount):
    #             pg.draw.rect(window, BLACK, (c*hSIZE,r*hSIZE + hSIZE, hSIZE, hSIZE))
    #             pg.draw.circle(window, GRAY, (int(c*hSIZE+hSIZE/2), int(r*hSIZE+hSIZE+hSIZE/2)), hRADIUS)
    #     BOARD = board.history[i]
    #     for c in range(board.columnCount):
    #         for r in range(board.rowCount):
    #             if BOARD[r][c] == board.p1:
    #                 pg.draw.circle(window, RED, (int(c*hSIZE+hSIZE/2), int(r*hSIZE+hSIZE+hSIZE/2)), hRADIUS)
    #             if BOARD[r][c] == board.p2:
    #                 pg.draw.circle(window, BLUE, (int(c*hSIZE+hSIZE/2), int(r*hSIZE+hSIZE+hSIZE/2)), hRADIUS)
    pg.draw.rect(window, BLACK, (0,0,width, height))
    for i in range(len(board.results)):
        
        if board.results[i] == 1:
            text = hFont.render("Red Victory", 1, RED)
            window.blit(text, (50, placement))
            placement + 50
        if board.results[i] == 2:
            text = hFont.render("Blue Victory", 1, BLUE)
            window.blit(text, (50, placement))
            placement + 50
        if board.results[i] == 0:
            text = hFont.render("Tie Game", 1, GRAY)
            window.blit(text, (50, placement))
            placement + 50

BOARD = board.createBoard()
board.printBoard(BOARD)
isOver = False
turn = board.p2

pg.init()

SIZE = 100
RADIUS = int(SIZE/2-8)

hSIZE = 25
hRADIUS = int(hSIZE/2 - 2)

width = board.columnCount * SIZE
height = (board.rowCount+1)*SIZE
windowSize = (width, height)
placement = 50

window = pg.display.set_mode(windowSize)


font = pg.font.SysFont('monospace', 70)
sFont = pg.font.SysFont('monospace', 50)
hFont = pg.font.SysFont('monospace', 20)

start = False
space = False
history = False
result = -1

while not start:
    text = sFont.render("Press S to Start...", 1, GRAY)
    window.blit(text, (50, height/2))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                start = True

renderBoard(BOARD)
pg.display.update()

while not isOver:

    
    
    for event in pg.event.get(): 
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:

            
            if event.key == pg.K_SPACE and space == False:
                print("Pause")
                space = True
                mouseListener.start()
                pg.draw.rect(window, BLACK, (0,0,width, height))
                text = font.render("Pause Game...", 1, GRAY)
                window.blit(text, (50, height/2))
            elif (event.key == pg.K_SPACE and space == True):
                    print("Resume")
                    space = False
                    mouseListener.stop()
                    renderBoard(BOARD)
                    pg.display.update()
            
            if event.key == pg.K_f and turn == board.p2:
                text = font.render("Player 2 Wins!", 1, BLUE)
                window.blit(text, (50, 10))
                board.score2 = board.score2 + 1
                result = 2
                print(board.score2)
                isOver = True
            elif event.key == pg.K_f and turn == board.p1:
                text = font.render("Player 1 Wins!", 1, RED)
                window.blit(text, (50, 10))
                board.score1 = board.score1 + 1
                result = 1
                print(board.score2)
                isOver = True

            if event.key == pg.K_h and history == False:
                pg.draw.rect(window, BLACK, (0,0,width, height))
                renderHistory()
                history = True
                print(history)
            if (event.key == pg.K_h and history == True):
                history == False
                print(history)
                renderBoard(BOARD)
                pg.display.update()
                    
            
            
                
                

        if event.type == pg.MOUSEMOTION:
            pg.draw.rect(window, BLACK, (0,0, width, SIZE))
            x = event.pos[0]
            if turn == board.p1:
                pg.draw.circle(window, BLUE, (x, int(SIZE/2)), RADIUS)
            
            if turn == board.p2:
                pg.draw.circle(window, RED, (x, int(SIZE/2)), RADIUS)
        
        pg.display.update()

        if event.type == pg.MOUSEBUTTONDOWN:
            pg.draw.rect(window, BLACK, (0,0, width, SIZE))

            if turn != 0:
                if turn == board.p1:
                    turn = board.p2
            
                elif turn == board.p2:
                    turn = board.p1

            #Player 1 Move
            if turn == board.p1:
                x = event.pos[0]
                c = int(math.floor(x/SIZE))

                if board.isValid(BOARD, c):
                    r = board.getOpenRow(BOARD, c)
                    board.dropPiece(BOARD, r, c, board.p1)

                    if board.winningMove(BOARD, board.p1):
                        text = font.render("Player 1 Wins!", 1, RED)
                        window.blit(text, (50, 10))
                        board.score1 = board.score1 + 1
                        result = 1
                        print(board.score1)
                        isOver = True
                    elif board.tie(BOARD):
                        text = font.render("Tie Game!", 1, GRAY)
                        window.blit(text, (50,10))
                        result = 0
                        isOver = True
                else:
                    turn = board.p2

            #Player 2 Move
            elif turn == board.p2:
                x = event.pos[0]
                c = int(math.floor(x/SIZE))

                if board.isValid(BOARD, c):
                    r = board.getOpenRow(BOARD, c)
                    board.dropPiece(BOARD, r, c, board.p2)

                    if board.winningMove(BOARD, board.p2):
                        text = font.render("Player 2 Wins!", 1, BLUE)
                        window.blit(text, (50, 10))
                        board.score2 = board.score2 + 1
                        result = 2
                        print(board.score2)
                        isOver = True
                    elif board.tie(BOARD):
                            text = font.render("Tie Game!", 1, GRAY)
                            window.blit(text, (50,10))
                            result = 0
                            isOver = True
                else:
                    turn = board.p1
            
            board.printBoard(BOARD)
            renderBoard(BOARD)
            space = False

    while isOver:
        board.addToHistory(BOARD, result)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_e or event.key == pg.K_ESCAPE:
                    print(result)
                    renderHistory()
                    pg.display.update()
                    
                if event.key == pg.K_s:
                    BOARD = board.clearBoard(BOARD)
                    renderBoard(BOARD)
                    pg.display.update()
                    turn = board.p2
                    isOver = False

                
