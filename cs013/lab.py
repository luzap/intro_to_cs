import random
import helpers

#
# Each of the following functions have an arbitrary return value. Your
# job is to edit the functions to return the correct value. You'll
# know it's correct because when you run test.py, the program will
# print "PASS" followed by the function name.
#
# Any code you add outside of these functions (in the global
# namespace) should be commented out before running test.py
#


def exponentiate(base, power):
    """Recursively obtain the result of an exponentiation operation."""
    if power > 0:
        return base * exponentiate(base, power - 1)
    else:
        return 1


def get_nth(list_of, n):
    """Get nth element of a list without slicing."""
    if n:
        # Why does this need a return statement?
        return get_nth(helpers.tail(list_of), n - 1)

    else:
        return helpers.head(list_of)


def reverse(list_of):
    if len(list_of) == 2:
        return helpers.tail(list_of) + [helpers.head(list_of)]
    else:
        return reverse(helpers.tail(list_of)) + [helpers.head(list_of)]


def is_older(date_1, date_2):
    if len(date_1):
        if helpers.head(date_1) < helpers.head(date_2):
            return True
        else:
            return is_older(helpers.tail(date_1), helpers.tail(date_2))
    else:
        return False


def number_before_reaching_sum(total, numbers):
    pass


def what_month(day):
    return 0
