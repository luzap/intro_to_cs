"""Exercise 1.5: More string reversal."""

# Reversal using for-loop
initial = 'When the saints go marching in'
new_string = ''

for char in initial:
    new_string = char + new_string

print("For loop reversal:", new_string)

# Reversal using while-loop
initial = 'When the saints go marching in'
new_string = ''

pos = 0
while pos < len(initial):
    new_string = initial[pos] + new_string
    pos += 1

print("While loop reversal:", new_string)
