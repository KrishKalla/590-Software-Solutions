import numpy as np
import math

gameOver = False
turn = 1

empty = 0
p1 = 1
p2 = 2

rowCount = 6
columnCount = 7

def createBoard():
    board = np.zeros((rowCount, columnCount))
    return board

def dropPiece(board, r, c, piece):
    board[r][c] = piece

def isValid(board, c):
    return board[rowCount - 1][c] == empty

def getOpenRow(board, c):
    for r in (range(rowCount)):
        if board[r][c] == empty:
            return r

def printBoard(board):
    print(np.flip(board, 0))

def winningMove(board, piece):
    #Check Horizontal Win
    for c in range (columnCount - 3):
        for r in range(rowCount):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    #Check Vertical Win
    for c in range(columnCount):
        for r in range(rowCount - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    #Check Diagonal Win(s)
    for c in range(columnCount - 3):
        for r in range(rowCount - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
            
    for c in range(columnCount - 3):
        for r in range(3, rowCount):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
def tie(board):
    for c in range(columnCount):
        for r in range(rowCount):
            if board[r][c] == empty:
                return False
    return True


