from IPython.display import clear_output
import random 

def display_board(board):
    # Clears the output to display the updated board (works in Jupyter notebooks)
    clear_output()
    
    # Displaying the Tic Tac Toe board with current markers
    # Here index 0 exists but it is not used !
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def player_input():
    # Prompt for player to select their marker
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    # Returns a tuple with both player markers (Player 1 and Player 2)
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
def place_marker(board, marker, position):
    # Places the player's marker on the selected position
    board[position] = marker

def win_check(board, mark):
    # Checks all possible winning combinations for the given marker
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the bottom
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # down the left side
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # down the middle
            (board[3] == mark and board[6] == mark and board[9] == mark) or  # down the right side
            (board[1] == mark and board[5] == mark and board[9] == mark) or  # diagonal
            (board[3] == mark and board[5] == mark and board[7] == mark))    # diagonal

def choose_first():
    # Randomly selects which player goes first
    return 'Player 1' if random.randint(0, 1) == 0 else 'Player 2'
    
def space_check(board, position):
    # Checks if a specific position on the board is available
    return board[position] == ' '

def full_board_check(board):
    # Returns True if all positions are filled; otherwise, returns False
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    # Prompt for player's move choice with validation
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
            position = int(input('Choose your next position: (1-9) '))
        except ValueError:
            print("Please enter a valid integer between 1 and 9.")
            
    return position

def replay():
    # Asks if players want to replay; starts with 'y' confirms
    return input('Do you want to play again? Enter Yes or No: ').strip().lower().startswith('y')

# Main game flow begins here
print('Welcome to Tic Tac Toe!')

while True:
    # Initialize and reset the game board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No: ')
    
    game_on = play_game.lower().startswith('y')

    while game_on:
        if turn == 'Player 1':
            # Player 1's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player 2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! Player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    # If players don't want a rematch, the loop ends
    if not replay():
        break
