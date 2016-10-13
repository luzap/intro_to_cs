"""1.1 For-loop transformation."""
myString = "The quick brOwn fOx jumped over thE lAzy dog"

vowels = ['a', 'e', 'i', 'o', 'u']

vowel_count = 0
for char in myString.lower():
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)
