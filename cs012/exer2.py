"""Exercise 1.2: Number machines."""
from functools import reduce


def multiplier(nums: list) -> list:
    """Given a list, return a new list with each element duped."""
    final = []
    for item in nums:
        final.extend([item] * 2)
    return final


def consumer(nums: list) -> list:
    """Removes the first instance of the largest element."""
    maximum = max(nums)
    nums.remove(maximum)
    return nums


def blender(nums: list) -> list:
    """Return the sum of all numbers as a list."""
    final = [reduce(lambda x, y: x + y, nums)]
    return final


if __name__ == '__main__':
    c = consumer
    m = multiplier
    b = blender
    # Result is 50
    print(b(m(c(m(c([1, 2, 3, 4, 5, 6]))))))
    # Result is 121
    print(b(c(c(c(m(m(m(c(m([2, 4, 5]))))))))))
    # Result is 26
    print(b(m(c(m([1, 1, 1, 1, 5])))))
