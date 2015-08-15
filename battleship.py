from random import randint

maxSize = 8  # Dimension of battlefield

# Battleship board
board = []
for x in range( maxSize):
    board.append(["O"] * maxSize)
    
# Duplicate board for ship locations
ansBoard = []
for x in range( maxSize):
    ansBoard.append(["O"] * maxSize)


# Show the board to the players
def print_board( board):
    for row in board:
        print " ".join( row)

print "Let's play Battleship!"
#print_board( board)


# To choose random row/col
def random_row( board):
    return randint( 0, len( board) - 1)

def random_col(board):
    return randint( 0, len( board[0]) - 1)


# Check for free space
def ship_ok( board, row, col):
    if( board[row][col] == "X"):
        return True
    else:
        return False


#### Add a ship to the ansBoard #####
def add_ship( board, shipSize):

    while( True):
        print "START"
        row = random_row( board)
        col = random_col( board)
    
        # Don't start a new ship where one already is
        if( board[row][col] == "X"):
            row = random_row( board)
            col = random_col( board)

        board[row][col] = "X"  # place first part of a ship
        """print "row ", row, " col ", col"""
        direction = randint(0,1)  # vert. or horiz.

        count = shipSize - 1 # how many sections of the ship put down

        # vertical
        if( direction == 0):
            vert = True
            down = True
            up = True
            
            if( row + count >= maxSize):  # if it can't fit going down
                down = False
            if( row - count < 0):  # can't fit going up
                up = False

            if( down == True):
                for i in range( 1, shipSize):  # check down for Xs
                    if( board[row + i][col] == "X"):
                        print "DOWN = FALSE"
                        down = False
                        break
            if( up == True):
                for i in range( 1, shipSize):  # check up for Xs
                    if( board[row - i][col] == "X"):
                        up = False
                        print "UP = FALSE"
                        break

            if( down == False and up == False):  # can't go up or down
                vert = False

            if( down == True):  # is room and no Xs
                while( count > 0):
                    board[row + count][col] = "X"
                    count -= 1
                return
            if( up == True):  # is room and no Xs
                while( count > 0):
                    board[row - count][col] = "X"
                    count -= 1
                return
            
        # horizontal    
        if( direction == 1 or vert == False):  
            horiz = True
            right = True
            left = True

            if( col + count >= maxSize):  # if it can't fit going right
                right = False
            if( col - count < 0):  # can't fit going left
                left = False

            if( right == True):
                for i in range( 1, shipSize):  # check to right for Xs
                    if board[row][col + i] == "X":
                        right = False
                        print "RIGHT = FALSE"
                        break
            if( left == True):
                for i in range( 1, shipSize):  # check to left for Xs
                    if board[row][col - i] == "X":
                        left = False
                        print "LEFT = FALSE"
                        break

            if( right == False and left == False):  #can't go left or right
                print "go back to the beginning"
                board[row][col] = "O"
                continue  # to try vert

            if( right == True):  # is room and no Xs
                while( count > 0):
                    board[row][col + count] = "X"
                    count -= 1
                return
            if( left == True):  # is room and no Xs
                while( count > 0):
                    board[row][col - count] = "X"
                    count -= 1
                return


add_ship( ansBoard, 2)
add_ship( ansBoard, 3)
add_ship( ansBoard, 4)

print " ____answer key____ "
print_board(ansBoard)

"""
# Allow the player 4 turns maximum
for turn in range(4):
    
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess a Row:"))
    guess_col = int(raw_input("Guess a Col:"))

    if (ans_board[guess_row][guess_col] == "X"):
        print "Hit!"
        #break
    else:
        if (turn == 3):
            print "Game Over"
        elif (guess_row < 0 or guess_row > maxSize - 1) or \
        (guess_col < 0 or guess_col > maxSize - 1):
            print "That location is on some other planet."
        elif (board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "Miss!"
            board[guess_row][guess_col] = "X"
            print_board(board)
"""
