'''
Command Line Pente
'''


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
