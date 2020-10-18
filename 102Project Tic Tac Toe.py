# ============= GLOBAL VARIABLES ============

game_still_going = True   # this keeps game_still_going in the loop until the point where game is over . where this will become false.

winner = None     # WHO WON OR TIE?

current_player = "X"

# board layout
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# function to display board
def display_board():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])


def play_game():

    display_board()     # display initial board

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()   # check if game has ended

        flip_player()   # flip to the other player

    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!!")
    elif winner is None:
        print("Tie")


def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        # using if statement leads to this code running only one time.
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input! Choose any input from 1-9.")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there! Please try again. ")

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():

    global winner   # calling winner for global variables

    row_winner = check_rows()    # defining row winner variable and it checks rows
    column_winner = check_columns()    # defining column winner variable and it checks columns
    diagonal_winner = check_diagonals()    # defining diagonal winner variable and it checks digonals

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner

    return


def check_rows():

    global game_still_going    # called global variable from above

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]

    return


def check_columns():
    global game_still_going  # called global variable from above

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]

    return


def check_diagonals():
    global game_still_going  # called global variable from above

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]

    return


def check_for_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return


play_game()

# board
# play game
# check win
# handle turns
# check rows
# check columns
# check diagonals
