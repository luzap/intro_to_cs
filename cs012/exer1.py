"""Exercise 1.1: Tic-Tac-Toe Tie."""

# From last week's lab


def make_board(m, n, filler):
    """Creates a multidimensional arrya with the filler representing entries."""
    board = []
    for i in range(m):
        board.append([filler for i in range(n)])
    return board


def print_board(board: list) -> None:
    """Print the board using the tried and true method for board printing."""
    print("+" + "---+" * len(board[0]))
    for row in range(len(board)):
        print("| " + " | ".join(board[row]), end=" |\n")
        print("+" + "---+" * len(board[0]))


def update_board(board: list, i: int, j: int, decorator: str, filler: str) -> list:
    """Update the board array with guess."""
    if board[i][j] == filler:
        board[i][j] = decorator
        return True
    else:
        return False


def iswinner(board: list, decorator: str) -> bool:
    """Determine whether or not someone has won."""
    checks = []
    check = lambda value: all(map(lambda x: str(x) == decorator, value))

    for row in board:
        checks.append(check(row))
    print(checks)

    t_board = zip(*board)
    for column in t_board:
        checks.append(check(column))

    for i in range(2):
        diagonal = []
        for j in range(len(board)):
            if i == 0:
                diagonal.append(board[i][i] is decorator)
            else:
                diagonal.append(board[-(j + 1)][-(j + 1)] is decorator)
            checks.append(all(diagonal))

    return any(checks)


def istie(board: list, filler: str) -> bool:
    """Check if there's a tie with no winner.'"""
    filled = 0
    for row in board:
        filled += sum(list(map(lambda x: x != filler, row)))
    return bool(1 * (filled == (len(board) * len(board[0]))))


round_nm = 0
playing = True
draw = False

filler = input("What filler character would you like? ")
board = make_board(3, 3, filler)

players = []
players.append(input("What character would player 1 like to be? ")[:1])
players.append(input("What character would plater 2 like to be? ")[:1])


while playing and not draw:
    print("Round", round_nm + 1)
    print_board(board)
    print("Player {}'s turn:".format(round_nm % 2 + 1))
    i, j = list(map(lambda x: int(x), input(
        "Where should I place your mark? ").split(',')))
    update_board(board, i, j, players[round_nm % 2], filler)

    round_nm += 1
    playing = not (iswinner(board, players[0]) or iswinner(board, players[1]))
    draw = istie(board, filler)
else:
    print("Player {} wins!".format((round_nm) % 2))
