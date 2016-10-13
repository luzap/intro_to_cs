"""Exercise 3: List interactions"""


def remove_whitespace(lst):
    """Remove whitespace from words after split."""
    final = [word.strip() for word in lst.split(",")]
    return final

# Sorted list
words = input("Please enter a list of words separated by commas: ")
words = sorted(remove_whitespace(words))

# Alternative method
# words = list(map(lambda x: x.strip(), words))
# (Returns a generator, so need to convert to list)

print(words)

# List extension
more_words = input("Please enter another list of words separated by commas: ")
words.extend(remove_whitespace(more_words))
print(words)

# Returning index of list and then removing the word from index
ind = input("Enter a word: ")
print("Word index: ", words.index(ind))
words.remove(ind)
print(words)
