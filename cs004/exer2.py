"""Exercise 2: Strings."""
string1 = 'The rain in Spain falls mainly on the plain'
print("Original phrase:", string1)

# Reversed
reverse = ''
for i in string1:
    reverse = i + reverse
print("Reversed:", reverse)

# Uppercase
final = ''
for i in string1:
    final += i.upper()
print("Uppercase:", final)


# Count
def custom_count(string1, search_string):
    """Count the number of occurences of a substring."""
    count = 0
    for index in range(0, len(string1)):
        phrase = string1[index:index + len(search_string)]
        count += (phrase == search_string)
    return count

print("Occurence of 'ai' in phrase:", custom_count(string1, "ai"))
