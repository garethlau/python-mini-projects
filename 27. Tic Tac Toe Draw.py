def get_player_entry(board_name, turn):
    lst_entry = []

    str_entry = input("Entry: ")
    lst_entry.append(str_entry[0])
    lst_entry.append(str_entry[2])

    if turn % 2 == 1:
        i = int(lst_entry[0]) - 1
        j = int(lst_entry[1]) - 1
        board_name[i][j] = 'X'
    else:
        i = int(lst_entry[0]) - 1
        j = int(lst_entry[1]) - 1
        board_name[i][j] = 'O'

    return lst_entry

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

get_player_entry(board, 2)
print(board)
print(get_player_entry(board, 3))
