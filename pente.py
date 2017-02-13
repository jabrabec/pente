'''
Command Line Pente

'''
import random


def make_board():
    '''Set up an "empty" 15x15 grid with headers'''

    # Define blank list
    board = []

    # Create header row
    header = ""
    for num in range(1, 16):
        header += (" " + str(num))
    board.append(header.split(" "))

    # Generate rows with length of 16
    for row in range(1, 16):
        # Append a blank list to each row cell
        board.append([])
        board[row].append(str(row))
        for column in range(1, 16):
            # Assign x to each row
            board[row].append('.')

    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(board[i][j]) < 2:
                board[i][j] = " " + board[i][j]

    return board


def print_board(board):
    '''Print board in grid layout'''

    for row in board:
        print " ".join(row)


def player_play(board, played=None):
    '''Play the game'''

    # check board for empty (' .') spaces and exit the game when none remain
    empty_count = 0
    for row in board[1:]:
        for space in row:
            if space == ' .':
                empty_count += 1
    if empty_count == 0:
        print "It's a tie!"
        return

    # initialize played as an empty set if nothing passed to func for this var
    if not played:
        played = set()

    # prompt player for row & column coordinates, restricting allowable entries
    player_row = raw_input('Pick a row (1-15): ')
    # ensure value is not None before converting to int
    if player_row:
        player_row = int(player_row)
    while player_row not in range(1, 16):
        player_row = raw_input('Please only choose numbers between 1-15: ')
        # ensure value is not None before converting to int
        if player_row:
            player_row = int(player_row)
    player_col = raw_input('Pick a column (1-15): ')
    # ensure value is not None before converting to int
    if player_col:
        player_col = int(player_col)
    while player_col not in range(1, 16):
        player_col = raw_input('Please only choose numbers between 1-15: ')
        # ensure value is not None before converting to int
        if player_col:
            player_col = int(player_col)

    # ensure player picked an available space, add it to the set of used spaces
    # set the marker at that space to 'X', print current state of board, check
    # if winning move, and alternate to computer's turn to play
    if board[player_row][player_col] == ' .':
        played = played | {(player_row, player_col)}
        board[player_row][player_col] = ' X'
        print_board(board)
        # if check_for_winner(board):
        #     return
        computer_play(board, played)
    # reprompt player to choose again if they picked a nonempty space
    elif (player_row, player_col) in played:
        print "You picked a nonempty space, please try again!"
        player_play(board, played)


def computer_play(board, played=None):
    '''Handle computer's moves'''

    # check board for empty (' .') spaces and exit the game when none remain
    empty_count = 0
    for row in board[1:]:
        for space in row:
            if space == ' .':
                empty_count += 1
    if empty_count == 0:
        print "It's a tie!"
        return

    # initialize played as an empty set if nothing passed to func for this var
    if not played:
        played = set()

    # computer picks a random row, col coordinate to play
    comp_row = random.randrange(1, 16)
    comp_col = random.randrange(1, 16)

    # ensure computer picked an available space, add it to the set of occupied,
    # set the marker at that space to 'O', print current state of board, check
    # if winning move, and alternate to player's turn to play
    if board[comp_row][comp_col] == ' .':
        played = played | {(comp_row, comp_col)}
        board[comp_row][comp_col] = ' O'
        print "The computer picked %s, %s." % (comp_row, comp_col)
        print_board(board)
        # if check_for_winner(board):
        #     return
        player_play(board, played)
    # call function again if computer picked a nonempty space
    elif (comp_row, comp_col) in played:
        computer_play(board, played)


def start_game():
    '''Initiates new game'''

    # make new empty board
    board = make_board()
    # print starting empty board
    print_board(board)
    # random choice between player and computer for first move
    if random.randint(0, 1) == 0:
        print "Player goes first!"
        player_play(board)
    else:
        print "Computer goes first!"
        computer_play(board)


# start a game when run from cmd line or interactively
start_game()
