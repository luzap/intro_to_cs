import helpers

# Your job is to develop this function


def find_path(board, row, col):
    if not helpers.islegal(board, row, col):
        return False

    if board[row][col] == "x":
        return True
    elif board[row][col] == ".":
        pass
    elif board[row][col] == 'o':
        pass
    else:
        return False

    board[row][col] = "*"
    if find_path(board, row + 1, col):
        return True

    if find_path(board, row - 1, col):
        return True

    if find_path(board, row, col + 1):
        return True

    if find_path(board, row, col - 1):
        return True

    return False


board = helpers.get_board('board.txt')


helpers.print_board(board)
print('-' * 50)

find_path(board, 0, 0)

print('-' * 50)
helpers.print_board(board)
