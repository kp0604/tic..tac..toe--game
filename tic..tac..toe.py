#------------------global variables---------------------------------------------

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

current_player = "X"

game_stillgoing = True

winner = None


#-----------we need a board-----------------------------------------------------

def display_board():

    print("\n") 
    print(board[0] + " | " + board[1] + " | " + board[2] + "   " + "1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "   " + "4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "   " + "7 | 8 | 9")
    print("\n")

#-----------------how will it put in the entries--------------------------------

def handle_turn():
    
    position = int(input('enter the position from 1-9 : '))

    position = position - 1
    if board[position] == '-':

        board[position] = current_player

    else:
        print("you can't choose that. go again")
        handle_turn()


#----------------------flip player----------------------------------------------

def flip_player():

    global current_player
    if current_player == "X":
        current_player = "O"
        print(f"{current_player}'s turn")
    elif current_player == "O":
        current_player = "X"
        print(f"{current_player}'s turn")


#---------------------------game over-------------------------------------------

def gameover():

    if checkforwin() or checkfortie():
        display_board()
        print(f'winner is {winner}')


#-------------------------check for Win-----------------------------------------

def checkforwin():

    global game_stillgoing
    global winner
    checkforcolumns()
    checkfordiagonals()
    checkforrows()
    if game_stillgoing == False:
        winner = current_player
        return winner


#----------------------------tie------------------------------------------------


def checkfortie():

    global winner
    global game_stillgoing

    if "-" not in board:
        game_stillgoing = False
        winner = None
        return True


#-------------------check for rows----------------------------------------------

def checkforrows():

    global game_stillgoing
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3 == True:
        game_stillgoing = False


#---------------------check for column-----------------------------------------

def checkforcolumns():

    global game_stillgoing
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3 == True:
        game_stillgoing = False


#--------------------check for diagonal-----------------------------------------

def checkfordiagonals():

    global game_stillgoing
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    if diagonal1 or diagonal2 == True:
        game_stillgoing = False


#--------------------------play game--------------------------------------------

def playgame():
    
    while game_stillgoing:

        display_board()

        flip_player()

        handle_turn()

        gameover()


#-------------------------------------------------------------------------------

playgame()
