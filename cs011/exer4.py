import requests
from string import punctuation


def search_for_string(url: str, search: str) -> int:
    text = requests.get(url).text
    line_count = len(text.split("\n"))

    filt = (list(punctuation) + ['\n'])

    for mark in filt:
        text = text.replace(mark, " ")
    text = list(filter(lambda x: x != "", text.split(" ")))

    step = len(search.split(" "))

    count = 0
    for word in range(0, len(text) - 1):
        sentence = " ".join(text[word: word + step]).strip().lower()
        if search.lower() == sentence:
            count += 1

    return (count, line_count)


# Tried against the find functionality in Chrome, delivers the same result
print(search_for_string(
    "http://www.textfiles.com/etext/FICTION/alice.txt", "Alice"))
