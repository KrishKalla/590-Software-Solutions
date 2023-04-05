import renderer
import logic
import sys
import constants
import math
import pygame as pg

start = False
menu = False
space = False
history = False
forfeit = False



options = [constants.CUSTOM1, constants.CUSTOM2, constants.BACKGROUND]
counter = 0

turn = constants.p1
result = 0

# #Start Screen
renderer.blank()
while not start and not menu:
    
    renderer.text("Press S to Start Game or Esc to Exit", 270, 50, constants.GRAY)

    renderer.text("Press Space to Enter Preferences", 500, 35, constants.GRAY)

    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                renderer.blank()
                start = True
            elif event.key == pg.K_SPACE:
                menu = True
            elif event.key == pg.K_ESCAPE:
                pg.quit()

    #Settings Menu
    while menu:
        renderer.blank()
        if counter == 0:
            renderer.text("Player 1 Color: " + str(constants.CUSTOM1), 50, 60, constants.CUSTOM1)
        if counter == 1:
            renderer.text("Player 2 Color: " + str(constants.CUSTOM2), 50, 60, constants.CUSTOM2)
        if counter == 2:
            renderer.text("Background Color: " + str(constants.BACKGROUND), 50, 60, constants.GRAY)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    menu = False
                    renderer.blank()
                if event.key == pg.K_RIGHT:
                    counter = counter + 1
                    if counter > 2:
                        counter = 0
                if event.key == pg.K_LEFT:
                    counter = counter - 1
                    if counter < 0:
                        counter = 2


board = logic.createBoard()
renderer.renderBoard(board)
renderer.scoreboard(constants.score1, constants.score2)


while not logic.gameOver:
    #Render the Board & Pieces
    print(pg.mouse.get_pos())
    

    if space == True:
        renderer.blank()
        renderer.text("Game Paused - Press Space to Continue", 350, 40, constants.WHITE)
            #inputs.stopMouse()

    if not space and not history and not logic.win and not forfeit:
        logic.printBoard(board)
        renderer.renderBoard(board)
        renderer.scoreboard(constants.score1, constants.score2)

    if logic.win == True:
        renderer.text("Press S to Play Again or Press Esc to Exit the Game", 500, 26, constants.WHITE)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    board = logic.clearBoard(board)
                    renderer.blank()
                    renderer.renderBoard(board)
                    turn = constants.p1
                    logic.win = False
                if event.key == pg.K_ESCAPE:
                    logic.gameOver == True
                    pg.quit()        


    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            #Pause/Resume Space Key Checker
            if event.key == pg.K_SPACE:
                if space == False:
                    space = True
                    print(space)
                elif space == True:
                    renderer.blank()
                    space = False
                    print(space)
            
            #Does not work - removed from final program due to constraints
            #History Key
            if event.key == pg.K_h:
                if history == False:
                    history = True
                if history == True:
                    history = False
            
            #Forfeit Key
            if event.key == pg.K_f:
                if turn == constants.p1:
                    renderer.blank()
                    renderer.text("Player 2 Wins", 270, 60, constants.BLUE)
                    result = 2
                    constants.score2 = constants.score2 + 1
                    logic.win = True
                    #Additions Required

                elif turn == constants.p2:
                    renderer.blank()
                    renderer.text("Player 1 Wins", 270, 60, constants.RED)
                    result = 1
                    constants.score1 = constants.score1 + 1
                    logic.win = True
                    #Additions Required

        if event.type == pg.MOUSEMOTION:
            x = event.pos[0]
            if turn == constants.p1:
                pg.draw.rect(renderer.window, constants.BACKGROUND, (0,0, constants.width, 2*constants.SIZE))
                pg.draw.circle(renderer.window, constants.RED, (x, int(constants.SIZE/2+constants.SIZE)), constants.RADIUS)
            if turn == constants.p2:
                pg.draw.rect(renderer.window, constants.BACKGROUND, (0,0, constants.width, 2*constants.SIZE))
                pg.draw.circle(renderer.window, constants.BLUE, (x, int(constants.SIZE/2+constants.SIZE)), constants.RADIUS)
        
        if event.type == pg.MOUSEBUTTONDOWN:
            pg.draw.rect(renderer.window, constants.BACKGROUND, (0,0, constants.width, constants.SIZE))

            if space == True:
                print("Still Paused")

            #Player 1 Move
            elif turn == constants.p1:
                x = event.pos[0]
                c = int(math.floor(x/constants.SIZE))
                print(c)
                if logic.isValid(board, c):
                    r = logic.getOpenRow(board, c)
                    logic.dropPiece(board, r, c, constants.p1)

                    if logic.winningMove(board, constants.p1):
                        renderer.blank()
                        renderer.text("Player 1 Wins", 270, 60, constants.RED)
                        result = 1
                        constants.score1 = constants.score1 + 1
                        logic.win = True

                    elif logic.tie(board):
                        renderer.blank()
                        renderer.text("Tie Game", 270, 60, constants.GRAY)
                        logic.win = True
                    else:
                        turn = constants.p2

            #Player 2 Move
            elif turn == constants.p2:
                x = event.pos[0]
                c = int(math.floor(x/constants.SIZE))

                if logic.isValid(board, c):
                    r = logic.getOpenRow(board, c)
                    logic.dropPiece(board, r, c, constants.p2)

                    if logic.winningMove(board, constants.p2):
                        renderer.blank()
                        renderer.text("Player 2 Wins", 270, 60, constants.BLUE)
                        result = 2
                        constants.score2 = constants.score2 + 1
                        logic.win = True

                    elif logic.tie(board):
                        renderer.blank()
                        renderer.text("Tie Game", 270, 60, constants.GRAY)
                        logic.win = True
                    else:
                        turn = constants.p1

        

        
            
            

