import random


def display_board(board):
    print('   |   | ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   | ')
    print('----------')
    print('   |   | ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   | ')
    print('----------')
    print('   |   | ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   | ')


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)


def player_input():
    '''
    OUTPUT = (PLAYER 1 marker , PLAYER 2 marker)
    '''

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("Player1: choose X or O: ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


player1_marker, player2_marker = player_input()
print(player1_marker)
print(player2_marker)


def place_marker(board, marker, position):
    board[position] = marker


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

place_marker(test_board, '$', 8)
display_board(test_board)


def win_check(board, mark):
    # WIN TIC TAC TOE

    # ALL ROWS, AND CHECK TO SEE IF THEY ALL SHARE THE SAME MARKER?
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the row
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the row
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the row
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the column
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the column
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the column
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


display_board(test_board)
print(win_check(test_board, 'X'))


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


print(choose_first())


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # if board is full then we return true
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9): '))
    return position


def replay():
    choice = input('Play again? Enter yes or no')

    return choice == 'yes'


# LAST PART

# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to TIC TAC TOE')

while True:

    # PLAY THE GAME

    ## SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X,O)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False


    ## GAME PLAY
    ### PLAYER ONE TURN

    while game_on:
        if turn == 'Player 1':

            # Shoe the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board,player1_marker,position)
            # Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    game_on = False
                else:
                    turn = 'Player 2'
        ### PLAYER TWO TURN
        else:
            # Show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break

    # BREAK OUT OF THE WHILE LOOP ON replay()
