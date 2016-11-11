"""
Verbal Arithmetic

Lukas Zapolskas, lz1477
"""
import random
from functools import partial
from operator import methodcaller


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


def guess(equation):
    """Returns a list of numbers from 0 to 9 not associated with a unique
    character.

    :param equation: list of strings
    :returns: list of integers
    """
    # Generates a list of numbers from 0 to 9 to be compared against
    # the numbers already used
    unused_numbers = [x for x in range(10)]
    for word in equation:
        for char in word:
            # Checks whether or not a numerical character has been removed
            # from the unused_numbers list
            if char.isdigit() and int(char) in unused_numbers:
                unused_numbers.remove(int(char))
    return unused_numbers


def replace(equation, number):
    """Replace some character in equations with a number.

    :param equation: list of strings
    :param number: int
    :returns: list
    """
    for word in equation:
        # Going from the last character of the first word and going from there
        chars = list(reversed(list(word)))
        for char in chars:
            if char.isalpha():
                # Returns upon finding the first rightmost character
                # that's not a number
                return list(map(methodcaller("replace", char, str(number)), equation))


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


def get_ending(string, char_index):
    """I was having some issues capturing the last character of a
    string when using string slicing, so I decided to reverse the string,
    take characters off of the start, and re-reverse it.

    :param string: str
    :param char_index: int (the position up to which slicing happens)
    :returns: str
    """
    return string[::-1][:char_index][::-1]


def reject(equation):
    """Reject possible solutions based upon how well the first several
    characters fit into the model.

    :param equation: list of strings
    :returns: bool
    """
    # check contains the numerical data found in the string
    check = []

    # construct is used to reconstruct the numeral in string
    # form, to allow for a later conversion
    construct = ""

    # For all of the words in the list leading up to the last one,
    # take each character, check if it's numerical, and if it is,
    # make it part of the constructor
    # Only consecutive integers are allowed !!!
    for word in equation[:-1]:
        word = reversed(list(word))
        for char in word:
            # Usage of ternary to decide when to stop executing the
            # loop
            addendum = char if char.isdigit() else ""
            if addendum == "":
                break
            # Reversed due to the order of iterating through
            # characters
            construct = addendum + construct
        if construct != "":
            # Only if something is added to the constructor,
            # added to the checklist
            check.append(construct)
        # Reset the value for construct
        construct = ""

    # The next step is to find out the number of characters in the
    # smallest string, and then check if the addition works purely
    # for that. This way, one does not need to know anything else
    # about the equation to check whether or not it works
    if len(check) > 1:
        nums_used = min(map(len, check))
    else:
        # I'm slightly not too sure about this step, but I think
        # it's needed to make sure that the reject will not
        # return False for cases when there has not been enough replacement
        return True

    # Usage of functools.partial to call function with values from an iterator
    # and a constant
    spec_check = list(map(partial(get_ending, char_index=nums_used), check))

    # The following gets the sum of all of the numbers, then converts it back into
    # a string and cuts it down to the required lenght
    cut_sum = get_ending(str(sum(map(int, spec_check))), nums_used)
    # The same done to the ending
    ending_value = get_ending(equation[-1], nums_used)

    # The inversion is more like semantic sugar. If something is rejected,
    # I make sure it returns a value of True, to reduce the amount of 
    # confusion in the logic
    return not (ending_value == cut_sum)


def solve(equation):
    """Using all of the functions implemented above, recursively replaces each
    character with a numeral and checks whether or not the following equation
    is solvable.

    :param equation: list of strings
    :param rejected: dictionary
    :returns: lists
    """
    if accept(equation):
        return equation
    elif not len(guess(equation)):
        return []

    possibilities = guess(equation)
    replacement = random.choice(possibilities)



if __name__ == "__main__":
    print(solve(create("equations/00.txt")))