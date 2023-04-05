import constants
import numpy as np
import math

gameOver = False
win = False
turn = 1

#Create The Board
def createBoard():
    board = np.zeros((constants.rowCount, constants.colCount))
    return board

#Clear the Current Board
def clearBoard(board):
    board = np.zeros((constants.rowCount, constants.colCount))
    return board

#Print the Current Board in the OUTPUT
def printBoard(board):
    print(np.flip(board,0))

#Check if Column is Valid
def isValid(board, c):
    return board[constants.rowCount - 1][c] == constants.empty

#Check if there is open Row in Column
def getOpenRow(board, c):
    for r in range(constants.rowCount):
        if board[r][c] == constants.empty:
            return r

#Drop Piece in Given Row and Column
def dropPiece(board, r, c, piece):
    board[r][c] = piece

#Check if there is a win by player on the board
def winningMove(board, piece):
    #Check Horizontal Win
    for c in range (constants.colCount - 3):
        for r in range(constants.rowCount):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    #Check Vertical Win
    for c in range(constants.colCount):
        for r in range(constants.rowCount - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    #Check Diagonal Win(s)
    for c in range(constants.colCount - 3):
        for r in range(constants.rowCount - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
            
    for c in range(constants.colCount - 3):
        for r in range(3, constants.rowCount):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

#Check if there is a tie on the board
def tie(board):
    for c in range(constants.colCount):
        for r in range(constants.rowCount):
            if board[r][c] == constants.empty:
                return False
    return True