### Code Academy ###

from random import randint

# prepare a board
board = []

for x in range(0, 5):
    board.append(["O"] * 5)

# print the board
def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

# Maximum Turns
TURNS = 10

 # helpers to randomly pick a battleship's location 
def random_row(board):
    return randint(0, len(board) - 1)
    
def random_col(board):
    return randint(0, len(board[0]) - 1)

# start the game
for turn in range(TURNS):
    print "-------------------Turn", turn + 1, '-------------------'
    
    # computer picks a random location
    while True:
        ship_row = random_row(board)
        ship_col = random_col(board)
        board[ship_row][ship_col]
        
        if board[ship_row][ship_col] != 'O':
            continue
        else:
            break
    
    # Player guesses the battleship's location
    while True:
        try:
            guess_row = int(raw_input("Guess Row:"))
            guess_col = int(raw_input("Guess Col:"))
            print ''
            guess_location = board[guess_row][guess_col]
        except (IndexError, ValueError) as e:
            print 'Error:', e
            print 'Please do it again'
            print ''
            continue
        else:
            break
    
    print 'ship_row', ship_row
    print 'ship_col', ship_col
    print ''
    board[ship_row][ship_col] = '.'  
            
    # got it right
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
        print ''
        board[ship_row][ship_col] = '$'
        print_board(board)
        print ''
        break
        
    # got it wrong
    elif board[guess_row][guess_col] =='X':
        print "You guessed that one already."
        print ''
        print_board(board)
        print ''
    else:
        if guess_row in range(5) and guess_col in range(5):
            print "You missed my battleship!"
            print ''
            board[guess_row][guess_col] = 'X'
            print_board(board) 
            print '' 
        else:
            print "Oops, that's not even in the ocean."
            print ''

if turn == TURNS - 1:         
    print 'GAME OVER'
    