"""Monopoly

Author: Lukas Zapolskas
NetID: lz1477

This is a purely text-based Monopoly implementation, attempting to adhere
to the rules of the original game as close as possible. 

Implementation goals:
- game loop
- heuristics(?)
-

"""
import random
import time

# Global variable to determine the type of the property without
# hard-coding them in
types_of_properties = enumerate(["street", "railroad", "utility"], start=1)


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
        integer_entries = [item for item in list(properties[0].keys())
                           if item not in ["owner", "name"]]
        for prop in properties:
            for name in integer_entries:
                prop[name] = int(prop[name])
        return properties


def get_players(n: int) -> list:
    """Generate n players with predefined starting conditions."""
    # Pieces from the traditional Monopoly, as per their wiki
    # TODO Add logic to make sure they do not repeat (noun parser? NLTK?)
    pieces = ["shoe", "hat", "car", "dog", "thimble",
              "battleship", "wheelbarrow", "cat"]
    players = []
    for player in range(n):
        # The name should be a unique identifier, so padding ensures uniqueness
        players.append({
            "name": random.choice(pieces) + "_" + str(random.randint(1, 100)),
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
    print("Player", player['name'])
    print("\tWallet:", player['balance'])
    print("\tPosition:", player['position'])
    properties = []
    for item in board:
        if item['owner'] == player['name']:
            properties.append(item['name'])
    if len(properties):
        print("\tProperties:")
        print("\t\t" + "\n".join(properties))


def move_player(player: dict, board: list, dice_roll: int) -> None:
    current_pos = 0
    location = player['position']
    for item in board:
        if item['name'] == location:
            current_pos = board.index(item)
    final_pos = (current_pos + dice_roll) % len(board)
    if final_pos <= current_pos:
        player['balance'] -= board[0]['rent']


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


def user_input(players_enum: list, turn: int) -> str:
    """Ask for user input and parse it down into options."""
    data = input("Player {} [m: move; p: print info; q: quit]\n> ".format(
        turn % len(players_enum)))
    data = data.strip()[0]
    return data


def gameloop():
    players = get_players(int(input("How many players are playing? ")))
    names = enumerate([player['name'] for player in players], start=1)
    for num, name in names:
        print("Player {} has chosen the {}".format(num, name))
    board = get_board("monopoly.csv")
    print(iswinner(players))
    turn = 1
    while not iswinner(players)[0]:
        action = user_input(names)

if __name__ == '__main__':
    gameloop()
