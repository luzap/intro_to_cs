"""
Verbal Arithmetic

Lukas Zapolskas, lz1477
"""
from random import choice


def create(eq_file):
    """Create a list of words via file IO.

    :param eq_file: string containng file path
    :returns: ordered list of words
    """
    # Context handler that takes care of automatically closing the file
    with open(eq_file) as fhandle:
        # List comprehension to remove newline characters from words
        words = [word.strip() for word in fhandle.readlines()]
    return words


def display(equation):
    """Display right justified equation.

    :param equation: ordered list of words
    :returns: None
    """
    # Creates the same list sorted by increasing length
    # The + 2 is done to take into accound the plus and
    # the whitespace around it
    spaces = len(sorted(equation, key=len)[-1]) + 2
    formatted = []

    # second_last checks whether or not the word being considered
    # is the second last in the list. If so, then the plus should
    # be added, and the amount of spaces. Newline characters
    # are added for ease of printing in the last step
    for word in equation:
        second_last = (equation.index(word) == len(equation) - 2)
        formatted.append("{}{}\n".format("+" * second_last +
                                         " " * (spaces - len(word) - 1 *
                                                second_last), word))
    # Insert the dashes between the last and the second to last element
    # Since this happens only once, I decided that having it outside
    # of the for-loop would make its purpose clearer
    formatted.insert(-1, "-" * spaces + "\n")
    print("".join(formatted))  # Print out the joined string
    guess(['A1B2C3', 'Z9'])
    print(replace(["HELLO", "WORLD", "TOOLS"], 9))


def guess(equation):
    """Returns a list of numbers from 0 to 9 not associated with a unique
    character.

    :param equation: list of strings
    :returns: list of integers
    """
    # Generates a list of numbers from 0 to 9 to be compared against
    # the numbers already used
    unused_numbers = [x for x in range(10)]

    # The equation can be given as a list
    for sequence in equation:
        # Splits a string into two character chuncks. Needed to obtain
        # the numeric character.
        sequence = [sequence[i:i + 2] for i in range(0, len(sequence), 2)]
        for pair in sequence:
            # Usage of str.isdigit() to determine whether or not the
            # character is convertible, otherwise assigning None via
            # a ternary operator (?)
            numeric = int(pair[-1]) if pair[-1].isdigit() else None
            # Removes used entries. If numeric is None, then nothing
            # happens, so an if-statement is not necessary
            unused_numbers.remove(numeric)
    return unused_numbers


def replace(equation, number):
    """Replace some character in equations with a number.
    :param equation: list of strings
    :param number: int
    :returns: list
    """
    for word in equation:
        chars = reversed(list(word))
        for char in chars:
            if char.isalpha():
                return list(map(lambda x: x.replace(char, str(number)), equation))


def accept(equation):
    """Checks for three conditions before deciding whether or not the proposed
    equation works.

    :param equation: list of strings
    :returns: bool
    """

    # Maps all strings to integers
    numeric = [int(x) for x in equation if x.isdigit()]

    # Checks for one-to-one mapping of equations to numeric
    if len(numeric) != len(equation):
        return False

    # Checks whether or not the sum of elements up to n - 1
    # is equal to n
    if sum(numeric[:-1]) != numeric[-1]:
        return False

    # Checks if the first values are non-zero
    if not all(filter(lambda x: int(x[0]) > 0, equation)):
        return False

    # If all of the tests pass, return True
    return True


def reject(equation):
    return False


def solve(equation):
    return []


if __name__ == "__main__":
    display(create("equations/00.txt"))
