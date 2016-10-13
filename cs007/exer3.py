"""Exercise 1.3: Binary addition."""

x = '1'
y = '111'


def bin_add(bin_string1: "str", bin_string2: "str") -> int:
    """Tentative addition of binary exploiting conversions."""
    if len(bin_string2) > len(bin_string1):
        bin_string1 = "0" * abs(len(bin_string2) - len(bin_string1)) + \
            bin_string1
    elif len(bin_string2) < len(bin_string1):
        bin_string2 = "0" * abs(len(bin_string1) - len(bin_string2)) + \
            bin_string2

    final_bin = 0
    for item in [bin_string1, bin_string2]:
        final_bin += int(item, base=2)  # I hope this isn't cheating
    final_bin = bin(final_bin)

    final_dec = 0
    for index in range(1, len(final_bin[2:]) + 1):
        final_dec += int(final_bin[-index]) * (2 ** (index - 1))
    return final_dec
