"""Monopoly

Author: Lukas Zapolskas
NetID: lz1477

This is a purely text-based Monopoly implementation, attempting to adhere
to the rules of the original game as close as possible.
"""
import random

# Global variable to determine the type of the property without
# hard-coding them in
types_of_properties = enumerate(["street", "railroad", "utility"], start=1)

# Global properties that cannot be bought and could be implemented to
# have different functionality
taboo = ['Community chest', 'Go', "Community chest", 'Income Tax']

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
            "balance": 1500,
            "position": "Go"
        })
    return players


def print_board(board: list, players: list) -> None:
    """Print the current state of the board."""
    for entry in board:
        print(entry["name"])
        if entry["owner"] not in ["", "bank"]:
            print("\tOwner:", entry["owner"])
        players_on_position = []
        for player in players:
            if player["position"] == entry["name"]:
                players_on_position.append(player['name'])
        if len(players_on_position):
            print("\tResidents:", ", ".join(players_on_position))


def print_player(player: dict, board: list) -> None:
    """Print the information about an individual player."""
    print(player['name'])
    print("\tWallet:", player['balance'])
    print("\tPosition:", player['position'])
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
    final_pos = (current_pos + dice_roll) % len(board)
    if final_pos < current_pos:
        # Add the money after passing Go
        players[index]['wallet'] -= board[0]['rent']
    # Assign position key a new value
    players[index]['position'] = board[final_pos]['name']
    return board[final_pos]['name']


def type_counter(player: dict, board: list, tile_type: int) -> int:
    pass


def iswinner(players: list) -> (bool, str):
    """Determine whether there is a winner by checking the balances of all players."""
    broke = 0
    for player in players:
        if player['balance'] == 0:
            broke += 1
        else:
            name = player['name']
    return (broke == (len(players) - 1)), name

##
# Custom functions
##


# TODO Type annotations
def pay_rent(players: list, index: int, owner_ind: int, location: str) -> None:
    """Subtract the rent from the balance of the moving player and add it to owner's balance."""
    rent = board[find_dict(location, board)]['rent']
    players[index]['wallet'] -= rent
    players[find_dict(board[owner_ind]['owner'], players)]['wallet'] += rent


def find_dict(attribute: str, dictionary: dict) -> int:
    """Return the index of dictionary that has a specific value."""
    for item in dictionary:
        if attribute in item.values():
            print(item.values())
            return dictionary.index(item)


def gen_movement(players: list, index: int, board: list):
    """Allow for player movement while keeping data persistance."""
    dice_roll = random.randint(2, 12)
    if pvp:
        print("You rolled a", dice_roll)
    location = move_player(players, index, board, dice_roll)
    owner = find_dict('owner', board)
    if owner is not None:
        pay_rent(players, index, owner)
    else:
        if (players[index]['balance'] >= board[find_dict(location, board)]['cost'])
        and (location not in taboo):
            yn = input("Would you like to buy the property?\n> ").strip()[0]
            if yn.lower() == 'y':
                players[index]['balance'] -= board[pos_index]['cost']
            else:
                print("Okay then. Stingy...")
        else:
            print("This property has no owner, but you're too broke to buy it. Oops.")


# TODO Convert this into something that would support heuristics
def core_gameloop() -> None:
    """Initial game loop which will then be abstracted to allow for computer input."""
    players = get_players(int(input("How many players are playing? ")))
    board = get_board("monopoly.csv")
    turn = 0
    print("Note that the default option is print player stats.")
    while not iswinner(players)[0]:
        print("Turn", (turn + 1))
        index = turn % len(players)
        data = input("{} [m: move; p: print info; q: quit]\n> ".format(
            players[index]['name']))
        action = data.strip()[0] if len(data) != 0 else "p"
        if action == 'm':
            gen_movement(players, index, board)
            turn += 1
        elif action == 'p':
            print_player(players[turn % len(players)], board)
        elif action == 'q':
            print("Sorry to see you leave so soon.")
            break
        else:
            print("Sorry, didn't quite catch that. And you skipped your turn!")
    else:
        print("The winner is", iswinner(players)[1])


if __name__ == "__main__":
    core_gameloop()
