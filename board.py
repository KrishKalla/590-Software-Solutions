# board Class
import numpy as np

RowCount = 6
ColumnCount = 7
Empty = 0


def create_board():
    """Function to create Board"""
    board = np.zeros((RowCount, ColumnCount))
    return (board)

def place_coin(board, row, col, player):
    """Function to Place Coin in Coordinate on Board Matrix"""
    board[row][col] = player

def valid_location(board, col):
    """Function to check whether invalid game move has been initiated by player"""
    return board[RowCount - 1][col] == Empty

def get_open_row(board, col):
    """Find Highest Open Row in the Column"""
    for i in range(RowCount):
        if board[i][col] == Empty:
            return i
        
def print_board(board):
    """Print textual version of the board"""
    print(np.flip(board,0))

def win(board, player):
    """Check every different possibility of winning"""
    #Horizontal Win Posibilities
    for c in range(ColumnCount-3):
        for r in range(RowCount):
            if board[r][c] == player and board [r][c+1] == player and board [r][c+2] == player and board [r][c+3] == player:
                return True


    #Vertical Win Posibilities
    for c in range (ColumnCount):
        for r in range (RowCount - 3):
            if board[r][c] == player and board [r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True

    #Diagonal Win Posibilities