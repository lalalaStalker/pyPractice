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


# Add a ship to the ansBoard
def add_ship( board, shipSize):
    row = random_row( board)
    col = random_col( board)
    
    # Don't start a new ship where one already is
    if( board[row][col] == "X"):
        row = random_row( board)
        col = random_col( board)

    board[row][col] = "X"  # place first part of a ship
    print "row ", row, " col ", col
    direction = randint(0,1)  # vert. or horiz.

    count = shipSize - 1 # how many sections of the ship put down

    # vertical
    if( direction == 0):  
        vert = True
        down = True
        
        if( row + count >= maxSize):  # if it can't fit going down
            down = False
        else:
            for i in range( 1, shipSize):  # check down for Xs
                if board[row + i][col] == "X":
                    vert = False
                    break
        if( vert == True and down == True):  # is room and no Xs
            print "num vert segments = ", count
            while( count > 0):
                board[row + count][col] = "X"
                count -= 1
        
    # horizontal    
    else:  
        horiz = True
        right = True

        if( col + count >= maxSize):  # if it can't fit going right
            right = False
        else:
            for i in range( 1, shipSize):  # check to right for Xs
                if board[row][col + i] == "X":
                    horiz = False
                    break
        if( horiz == True and right == True):  # is room and no Xs
            print "num horiz segments = ", count
            while( count > 0):
                board[row][col + count] = "X"
                count -= 1
"""           
    while( count < shipSize):
        if( direction == 0):
            if( row + 1 < maxSize):
                board[row + 1][col] = "X"
            else:
                board[row - 1][col] = "X"  #BAD- Bottom corner?
    else:
        if( col + 1 < maxSize):
            board[row][col + 1] = "X"    
        else:
            board[row][col - 1] = "X"
"""   
add_ship( ansBoard, 2)
add_ship( ansBoard, 2)

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
