'''
Check the status of the gameboard.
Returns 1 if player 1 one wins
Returns 2 if player 2 wins
Returns none if there is no winner
'''

def check_board(board):
    if board[0][0] == 1:  #top left corner is p1
        if board[0][1] == 1 and board[0][2] == 1:  #top row is p1
            return 1
        elif board[1][0] == 1 and board[2][0] == 1:  #left column is p1
            return 1
        elif board[1][1] == 1 and board[2][2] == 1:  #left diag in p1
            return 1
    elif board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
        return 1
    elif board[1][0] == 1 and board[1][1] == 1 and board [1][2] == 1:
        return 1

    if board[0][0] == 2:  # top left corner is p2
        if board[0][1] == 2 and board[0][2] == 2:  # top row is p2
            return 2
        elif board[1][0] == 2 and board[2][0] == 2:  # left column is p2
            return 2
        elif board[1][1] == 2 and board[2][2] == 2:  # left diag in p2
            return
    elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
        return
    elif board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
        return 2


if __name__=='__main__':

    board = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

    print(check_board(board))





