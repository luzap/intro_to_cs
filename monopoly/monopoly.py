"""Monopoly

Author: Lukas Zapolskas
NetID: lz1477

This is a purely text-based Monopoly implementation, attempting to adhere
to the rules of the original game as close as possible. 

Implementation goals:
- game loop
- purchase
- heuristics
    - optimal strategy of automatic purchase: ALL, NONE, RANDOM
    - 

"""
import random
import time
import argparse

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
        # I suppose I could just write in the three entries, but this is more fun
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
            "name": "Player_{}".format(player),
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


def user_input(player: str, turn: int) -> str:
    """Ask for user input and parse it down into options."""
    data = input("{} [m: move; p: print info; q: quit]\n> ".format(player))
    data = data.strip()[0]
    return data


# TODO Convert this into something that would support heuristics
def core_gameloop()-> None:
    """Initial game loop which will then be abstracted to allow for computer input."""
    players = get_players(int(input("How many players are playing? ")))
    board = get_board("monopoly.csv")
    turn = 1
    while not iswinner(players)[0]:
        print("Turn", turn)
        current_player = players[(turn - 1) % len(players)]
        action = user_input(current_player['name'])
        if action == 'm':
            pass
        elif action == 'p':
            print_player(player, board)
        elif action == 'q':
            print("Sorry to see you leave so soon.")
            break
        else:
            print("Sorry, didn't quite catch that. And you skipped your turn!")
    else:
        print("The winner is", iswinner(players)[1])


# # Command line options
# parser = argparse.ArgumentParser(
#     description="Start the game with varying gamemodes.")
# parser.add_argument('pvp', type=bool, default=True, re
#                     help="Run monopoly.py in player vs player or \
#                      heuristics mode.")
# args = parser.parse_args()

# if args.pvp or (args.pvp is None):
#     gameloop_main()
# else:
#     raise NotImplementedError(
#         "The functions responsible for this are not yet implemented.")

if __name__ == "__main__":
    core_gameloop()