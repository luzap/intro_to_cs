"""Exercise 2.3: Higher order functions."""
from functools import reduce

# Integers
numbers = list(range(1, 11))

# Addition
# Reduces the list to one value
sum_of_nums = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers from 1 to 10:", sum_of_nums)

# Multiplication
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers from 1 to 10:", product)

# Strings
string1 = 'The rain in Spain falls mainly on the plain'
print("Original phrase:", string1)

# Reverse - placeholder
rever = reduce(lambda x, y: x+y, string1)
print("Reversed (placeholder):", rever)

# Length - can it be condensed further?
length = reduce(lambda x, y: x + y, map(len, string1))
print("Length:", length)  # Tested against len - works

# Count - placeholder
count = ''.join(list(map(lambda x: x, string1)))
print("Count of 'ai' (placeholder):", count)

# Upper - complete
upper = "".join(map(lambda x: x.upper(), string1))
print("Uppercase: ", upper)
