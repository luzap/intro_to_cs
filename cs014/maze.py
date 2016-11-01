import helpers

# Your job is to develop this function
def find_path(board, row, col):
    next_cell = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col + 1)]

board = helpers.get_board('board.txt')
helpers.print_board(board)
print('-' * 50)

find_path(board, 0, 0)

print('-' * 50)
helpers.print_board(board)
