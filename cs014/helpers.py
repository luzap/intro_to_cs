def islegal(board, row, col):
    too_small = row < 0 or col < 0
    too_big = row >= len(board) or col >= len(board[row])
    
    return not too_big and not too_small

def get_board(fname):
    fp = open(fname)
    board = []
    for line in fp:
        board.append(list(line.strip()))
    fp.close()

    return board

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))

def debug(string, spaces):
    print(' ' * spaces, string)
