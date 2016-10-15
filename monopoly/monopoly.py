"""Monopoly

Author: Lukas Zapolskas
NetID: lz1477
"""
import random


def get_board(csv_file: str) -> list:
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
    # Pieces from the traditional Monopoly, as per their wiki
    pieces = ["shoe", "hat", "car", "dog", "thimble",
              "battleship", "wheelbarrow", "cat"]
    players = []
    for player in range(n):
        players.append({
            "name": random.choice(pieces),  # Randomly chosen element from list
            "balance": 1500,
            "position": "Go"
        })
    return players


def print_board(board: list, players: list) -> None:
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
    pass


def move_player(player: dict, board: list) -> None:
    pass


def type_counter(player: dict, board: list, tile_type: int) -> int:
    pass

if __name__ == '__main__':
    print_board(get_board("monopoly.csv"), get_players(2))
