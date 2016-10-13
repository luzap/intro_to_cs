"""Exercise 1.3: Rock-paper-scissors."""
import random

victory_condition = {
    "rock": "scissors",
    "paper":  "rock",
    "scissors": "paper",
}


def comp(hand1: str, hand2: str) -> int:
    """Compares the two victory_condition and returns either -1, 1, or 0."""
    print(hand1)
    print(hand2)
    if hand1 != hand2:
        if victory_condition[hand1] == hand2:
            return 1
        else:
            return -1
    else:
        return 0


def play(iterations: int, counter=0, p_games_won=0, comp_games_won=0, ties=0) -> list:
    """Plays a rock paper scissors game a specified number of times."""
    hands = list(victory_condition.keys())
    counter = 0
    while iterations != counter:
        hand1 = input("What's your hand? ")
        hand2 = hands[random.randint(0, 2)]
        score = comp(hand1, hand2)
        if score == 1:
            p_games_won += 1
            print("Player victory!")
        elif score == -1:
            comp_games_won += 1
            print("Computer victory! Better luck next time.")
        else:
            ties += 1
            print("You tied.")
        counter += 1
    return (p_games_won, comp_games_won, ties)

if __name__ == "__main__":
    results = play(3)

    print("You won {} games, you lost {} games and you tied {} games.".format(
        results[0], results[1], results[2]))
