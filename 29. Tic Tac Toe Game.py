def check_board(board):
    if board[0][0] == 'X':  #top left corner is p1
        if board[0][1] == 'X' and board[0][2] == 'X':  #top row is p1
            return 1
        elif board[1][0] == 'X' and board[2][0] == 'X':  #left column is p1
            return 1
        elif board[1][1] == 'X' and board[2][2] == 'X':  #left diag in p1
            return 1
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        return 1
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        return 1
    else:
        return 0
    if board[0][0] == 'O':  # top left corner is p2
        if board[0][1] == 'O' and board[0][2] == 'O':  # top row is p2
            return 2
        elif board[1][0] == 'O' and board[2][0] == 'O':  # left column is p2
            return 2
        elif board[1][1] == 'O' and board[2][2] == 'O':  # left diag in p2
            return
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        return
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        return 2
    else:
        return 0

def get_player_entry(board_name, turn):
    valid = False
    while not valid:
        entry = input("Enter a point: ")
        if len(entry) != 3:
            print("Sorry, I didn't catch that. Please try again: ")
            continue

        i = int(entry[0]) - 1
        j = int(entry[2]) - 1

        if board_name[i][j] == 'X':
            if turn % 2 == 1:
                print("You already have a token there! Please enter another point: ")
            else:
                print("That spot is already taken. Please enter another point: ")
        elif board_name[i][j] == 'O':
            if turn % 2 == 1:
                print("That spot is already taken. Please enter another point: ")
            else:
                print("You already have a token there! Please enter another point: ")
        else:
            valid = True
    if turn % 2 == 1:
        board_name[i][j] = 'X'
    else:
        board_name[i][j] = 'O'

def create_board(width):
    board = []
    for i in range(0, width):
        row = []
        for n in range(0, width):
            row.append('-')
        board.append(row)
    return(board)

def print_board(board):
    print("GAME BOARD")
    for i in range(0, len(board)):
        print(board[i][0] + board[i][1] + board[i][2])

if __name__=='__main__':

    print("       TIC TAC TOE")
    print("        __________")
    print("Enter the coordinates of \n"
          "your point as 'n,m' where \n"
          "n is the row number and m \n"
          "is the column number. For \n"
          "example, the input '1,1' \n"
          "would be the top left corner \n"
          "of the board. Have fun!")

    game = create_board(3)
    #print(game)
    print_board(game)

    turn = 1
    while check_board(game) == 0:
        if turn % 2 == 1:
            print("Turn: Player 1 (X)")
        else:
            print("Turn: Player 2 (O)")
        get_player_entry(game, turn)
        print_board(game)
        turn += 1

    if check_board(game) == 1:
        print("Player 1 wins!")
    elif check_board(game) == 2:
        print("Player 2 wins!")