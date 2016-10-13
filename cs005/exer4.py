"""Exercise 1.4: Random words."""
import random

rand_words = []
word_num = random.randint(1, 50)
new_string = ""

for word in range(word_num):
    for char in range(random.randint(3, 8)):
        new_string += chr(random.randint(97, 122))
    rand_words.append(new_string)
    new_string = ""


for word in rand_words:
    print(word)
