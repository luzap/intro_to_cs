"""Monopoly

Author: Lukas Zapolskas
NetID: lz1477

This is a purely text-based Monopoly implementation, attempting to adhere
to the rules of the original game as close as possible.

The function declarations given in the GitHub description have been altered
slightly by adding the the index variable, and passing the list of players.
This was done to make the data persistent, as passing the player when not
in the list would require replacement, and this way, the functions are
more self contained.
"""
import random

##
# Functions required by assignment
##


def get_board(csv_file: str) -> list:
    """Read the CSV file containing the board."""
    with open(csv_file, "r") as fhandle:
        headers = fhandle.readline().strip().split(",")
        properties = []

        # Main dictionary constructor
        for line in fhandle.read().split("\n"):
            values = line.strip().split(",")
            # Dictionary comprehension to avoid second for loop
            prop = {headers[index]: values[index]
                    for index in range(len(values))}
            properties.append(prop)

        # Conversion of string to integer types
        # I suppose I could just write in the three entries, but this is more
        # fun
        integer_entries = [item for item in list(properties[0].keys())
                           if item not in ["owner", "name"]]
        for prop in properties:
            for name in integer_entries:
                prop[name] = int(prop[name])
        return properties


def get_players(n: int) -> list:
    """Generate n players with predefined starting conditions."""
    # Pieces from the traditional Monopoly, as per their wiki
    players = []
    for player in range(n):
        # The name should be a unique identifier, so padding ensures uniqueness
        players.append({
            "name": "Player {}".format(player + 1),
            "wallet": 1500,
            "position": "Go"
        })
    return players


def print_board(board: list, players: list) -> None:
    """Print the current state of the board."""
    for entry in board:
        print(entry["name"])
        if entry["owner"] not in ["", "bank"]:
            print("\tOwner:", entry["owner"])

        # Print players in a certain position
        players_on_position = []
        for player in players:
            if player["position"] == entry["name"]:
                players_on_position.append(player['name'])

        # If there are any players in the position, print
        if len(players_on_position):
            print("\tResidents:", ", ".join(players_on_position))


def print_player(player: dict, board: list) -> None:
    """Print the information about an individual player."""
    # Values associated with the player
    print(player['name'])
    print("\tWallet:", player['wallet'])  # Tab character shifts alignment
    print("\tPosition:", player['position'])

    # Values associated with the board
    properties = []
    for item in board:
        if item['owner'] == player['name']:
            properties.append(item['name'])
    if len(properties):
        print("\tProperties:")
        print("\t\t" + "\n".join(properties))


def move_player(players: list, index: int, board: list, dice_roll: int) -> str:
    """Move the players on the board."""

    current_pos = 0
    location = players[index]['position']

    for item in board:  # Determine the current position of the player
        if item['name'] == location:
            current_pos = board.index(item)

    # Wrap around
    final_pos = (current_pos + dice_roll) % len(board)

    # Add the money after passing Go
    if final_pos < current_pos:
        players[index]['wallet'] -= board[0]['rent']

    # Assign position key a new value
    players[index]['position'] = board[final_pos]['name']
    print("{} arrived at {}".format(players[index]['name'],
                                    board[final_pos]['name']))
    return board[final_pos]['name']


def type_counter(players: dict, index: int, board: list, tile_type: int) -> int:
    count = 0
    player_name = players[index]['name']
    for item in board:
        if (item['owner'] == player_name) and (item['type'] == tile_type):
            count += 1


def iswinner(players: list) -> (bool, str):
    """Determine whether there is a winner by checking the balances of all players."""
    broke = 0
    for player in players:
        if player['wallet'] == 0:
            broke += 1
        else:
            name = player['name']
    return (broke == (len(players) - 1)), name

##
# Custom functions
##


def pay_rent(players: list, index: int, board: list, owner: str,
             loc_index: int) -> None:
    """Subtract the rent from the balance of the moving player and add it to
    owner's balance."""

    rent = board[loc_index]['rent']
    players[index]['wallet'] -= rent
    for player in players:
        if player['name'] == owner:
            owner_ind = players.index(owner)

    players[index]['wallet'] += rent
    print("{} payed {} to {} in rent".format(players[index]['name'], rent,
                                             players[owner_ind]['name']))


def find_dict(attribute: str, dictionary: dict) -> int:
    """Return the index of dictionary that has a specific value."""
    for item in dictionary:
        if attribute in item.values():
            return dictionary.index(item)


def gen_movement(players: list, index: int, board: list):
    """Allow for player movement while keeping data persistance."""
    dice_roll = random.randint(2, 12)  # Two dice
    print("You rolled a", dice_roll)
    location = move_player(players, index, board, dice_roll)
    loc_index = find_dict(location, board)

    # If owner of tile exists, he needs to be found
    owner_ind = 0
    for item in board:
        if location in item.values():
            owner_ind = board.index(item)

    # Taking care of purchasing and renting
    if owner_ind is not None:
        owner = board[owner_ind]['owner']
        if owner == 'bank':
            if players[index]['wallet'] >= \
                    board[loc_index]['cost'] and board[loc_index]['type'] > 0:
                yn = input("""It seems your balance is sufficient to buy this
property. Would you like to do so? """).strip()[0]
                if yn.lower() == 'y':  # Lowercase ensures match
                    players[index][
                        'wallet'] -= board[find_dict(location, board)]['cost']
                    board[find_dict(location, board)][
                        'owner'] = players[index]['name']
                    print("You have successfully purchased this property!")
                else:
                    print("Stingy...")
        else:
            if board[loc_index]['type'] > 0:
                pay_rent(players, index, board, owner, loc_index)


def gameloop() -> None:
    """Initial game loop which will then be abstracted to allow for computer input."""
    players = get_players(int(input("How many players are playing? ")))
    board = get_board("monopoly.csv")
    turn = 0
    print("Note that the default option is print player stats.")
    while not iswinner(players)[0]:
        for player in players:
            if player['wallet'] <= 0:
                print("{} is broke and can no longer participate!")
                players.remove(player)
                for prop in board:
                    if prop['owner'] == player['name']:
                        prop['owner'] = 'bank'
        print("\nTurn", (turn + 1))
        index = turn % len(players)
        data = input("{} [m: move; p: player info; b: board; q: quit;]\n> ".format(
            players[index]['name']))
        action = data.strip()[0] if len(data) != 0 else "p"
        if action == 'm':
            gen_movement(players, index, board)
            turn += 1
        elif action == 'p':
            print_player(players[turn % len(players)], board)
        elif action == 'b':
            print_board(board, players)
        elif action == 'q':
            print("Sorry to see you leave so soon.")
            break
        else:
            print("Sorry, didn't quite catch that. Please try again!")
    else:
        print("The winner is", iswinner(players)[1])


if __name__ == "__main__":
    gameloop()
