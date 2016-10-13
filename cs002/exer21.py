"""Exercise 2.1: Bob Barker."""

phrase = "BOB! Come get Bob's bobblehead"  # The original phrase
name = "bob barker"  # The replacement phrase

# Makes matching simpler
lower_phrase = phrase.lower()

print("Original: ", phrase)
print("Modified: ", lower_phrase.replace("bob", name))
