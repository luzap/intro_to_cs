"""Exercise 2.2: Cesar cipher."""
import filecmp
import string

shift = 3

input_file = "original.txt"
encrypted_file = "encrypted.txt"

# Using ord and chr


# Using translations
# Handle input from file
with open(input_file, "r+") as fhandle:
    text = "".join(fhandle.readlines())

# Make translation dictionary
alphabet = list(string.ascii_lowercase)

shifted = alphabet[shift:len(alphabet)] + alphabet[:shift]
translation = str.maketrans("".join(alphabet), "".join(shifted))

new_text = text.translate(translation)

with open(encrypted_file, "w+") as fhandle:
    fhandle.write(new_text)

with open(encrypted_file, "r+") as fhandle:
    enc_text = "".join(fhandle.readlines())

reverse_translation = str.maketrans("".join(shifted), "".join(alphabet))

decrypted_text = enc_text.translate(reverse_translation)
