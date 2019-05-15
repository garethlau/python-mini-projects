def create_board(width):
    board = []
    for i in range(0,width):
        row = []
        for n in range(0, width):
            row.append('-')
        board.append(row)
    return(board)

def print_board(board):

    for i in range(0, len(board)):
        print(board[i][2] + board[i][1] + board[i][2])


board = create_board(3)
print(board)
print_board(board)

