"""Exercise 2.1: Dragon slaughter"""
from random import randint
from labhelpers import dragon_color, dragon_breed

dragon_enclosure = {}

# Initial generation
i = 0
while len(dragon_enclosure.keys()) != 300:
    dragon = {
        "color": dragon_color[randint(0, len(dragon_color) - 1)],
        "age": str(randint(0, 100)),
        "breed": dragon_breed[randint(0, len(dragon_breed) - 1)],
        "size": str(randint(0, 20))
    }
    dragon_enclosure[i] = dragon
    i += 1

# Query mechanism
print("Welcome to the Dragon Querier, your one stop shop for all dragon "
      "related queries. Keywords are 'color', 'size', 'breed' and 'age'. "
      "Type 'stop' to stop anytime")

while True:
    i = 0
    user_query = input("Query: ")
    if user_query == "stop":
        break
    else:
        user_query = user_query.split(" ")
        if len(user_query) == 2:
            for dragon in dragon_enclosure.values():
                if dragon[user_query[0]] == user_query[1]:
                    i += 1

            print("{} such dragons in the enclosure.".format(i, user_query[1]))
        else:
            print("Something went wrong with your query. Please try again.")

print("Not enough? Wishing you had more statistical info on these dragons? "
      "Well, look no further! Here's a size breakdown by breed.")

# Initial statistics
breed_breakdown = {}
for breed in dragon_breed:
    breed_breakdown[breed] = 0
i = 0
for breed in dragon_breed:
    for dragon in dragon_enclosure.values():
        if dragon['breed'] == breed:
            breed_breakdown[breed] += 1

for key, value in breed_breakdown.items():
    print(key, "->", value)

dragon_age = 0
for dragon in dragon_enclosure.values():
    dragon_age += int(dragon['age'])

print("")
print("Average dragon age:", round(dragon_age / len(dragon_enclosure)))

dragon_size = 0
for dragon in dragon_enclosure.values():
    dragon_size += int(dragon['size'])

print("Average dragon size:", round(dragon_size / len(dragon_enclosure)))

print("")
print("Breed breakdown by percentage:")
for key, value in breed_breakdown.items():
    print(key, '->', round(value / len(dragon_enclosure) * 100, 2), "%")

print("\nAfter an unfortunate event that reduced their population to a third, \n"
      "the following numbers give a rough idea of what kind of dragons survived.\n")
# Deathmatches
reduced_dragon_enclosure = {}
reduced_dragon_enclosure_stats = {
    "age": 0,
    "breed": {},
    "color": "",
    "size": 0
}


i = 0
for num in range(0, len(dragon_enclosure), 3):
    match_1 = dragon_enclosure[num] if int(dragon_enclosure[num + 1]['size']) \
        < int(dragon_enclosure[num]['size']) else dragon_enclosure[num + 1]
    match_2 = match_1 if int(dragon_enclosure[num + 2]['size']) \
        < int(match_1['size']) else dragon_enclosure[num + 2]

    reduced_dragon_enclosure[i] = match_2
    i += 1

# Not sure these were the required statistics
for breed in dragon_breed:
    reduced_dragon_enclosure_stats["breed"][breed] = 0
i = 0

for breed in dragon_breed:
    for dragon in reduced_dragon_enclosure.values():
        if dragon['breed'] == breed:
            reduced_dragon_enclosure_stats["breed"][breed] += 1

for key, value in reduced_dragon_enclosure_stats["breed"].items():
    print(key, "->", value)

dragon_age = 0
for dragon in reduced_dragon_enclosure.values():
    dragon_age += int(dragon['age'])

print("")
print("Average dragon age:", round(dragon_age / len(reduced_dragon_enclosure)))

dragon_size = 0
for dragon in reduced_dragon_enclosure.values():
    dragon_size += int(dragon['size'])

print("Average dragon size:", round(dragon_size / len(reduced_dragon_enclosure)))
