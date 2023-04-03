import numpy as np
import math
import pygame as pg
import sys

rowCount = 6
columnCount = 7

empty = 0
p1 = 1
p2 = 2

def createBoard():
    board = np.zeros((6,7))
    return board

def isValidPosition(board, position):
    for r in range(rowCount):
        if board[r][position] == empty:
            return True
    return False

def dropPiece(board, position):
    for r in range (rowCount):
        if board[r][position] == empty:
            