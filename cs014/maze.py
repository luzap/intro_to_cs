import helpers

# Your job is to develop this function


def find_path(board, row, col):
    # Possible cells for movement. Limited to a
    paths = [(row - 1, col), (row, col - 1),
             (row + 1, col), (row, col + 1)]

    next_cells = [cell for cell in paths if helpers.islegal(board, cell[
                                                            0], cell[1])]

    next_cells = [cell for cell in next_cells if board[
        cell[0]][cell[1]] == "."]

    victory = any(
        list([victor for cell in next_cells if board[cell[0]][cell[1]] == "x"]))

    print(next_cells)

    if not victory:
        if not len(next_cells):
            return False
        elif len(next_cells) == 1:
            row, col = next_cells[0]
            board[row][col] = "*"
            find_path(board, row, col)
        else:
            for item in next_cells:
                row, col = item
                board[row][col] = "*"
                find_path(board, item[0], item[1])
    else:
        return True


board = helpers.get_board('board.txt')


helpers.print_board(board)
print('-' * 50)

find_path(board, 0, 0)

print('-' * 50)
helpers.print_board(board)
