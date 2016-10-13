"""Exercise 1.1: Fahrenheit to Celsius."""


def fahrenheit_to_celsius(fahrenheit: int) -> float:
    celsius = (fahrenheit - 32) / 1.8
    return celsius


def celsius_to_fahrenheit(celsius: int) -> float:
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit


print(fahrenheit_to_celsius(32))
print(celsius_to_fahrenheit(0))


def reverse_list(x: list) -> list:
    y = []
    for item in x:
        y = [item] + y
    return y


x = [1, 2, 3, 4, 5]
print(reverse_list(x))
