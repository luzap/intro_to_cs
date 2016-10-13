"""Exercise 1.1: CSV Dragons."""


def breakdown_by_property(members: list, prop: str) -> dict:
    """Shortening of the breakdown process."""
    breakdown = {}
    for member in members:
        if member[prop] not in breakdown.keys():
            breakdown[member[prop]] = []
        else:
            breakdown[member[prop]].append(member)
    return breakdown


dragons = []

# File IO
with open("dragons.csv", "r") as fhandle:
    headers = fhandle.readline().strip().split(",")
    for line in fhandle.readlines():
        drag = {}
        line = line.strip().split(",")
        for item in range(len(line)):
            drag[headers[item]] = line[item]
        dragons.append(drag)

print(len(dragons))

# Dragon stats
tot_size = 0
for dragon in dragons:
    tot_size += len(dragon['name'])

print("Average length of a dragon name: ", round(tot_size / len(dragons), 2),
      end="\n\n")

breed_breakdown = breakdown_by_property(dragons, 'breed')

print("Breed breakdown:")
for key in breed_breakdown.keys():
    print(key, len(breed_breakdown[key]), sep=', ')

max_size = 0

for dragon in dragons:
    if int(dragon['size']) > max_size:
        max_size = int(dragon['size'])

biggest = []

for dragon in dragons:
    if int(dragon['size']) == max_size:
        biggest.append(dragon)

breeds = {}  # What would be the best way of doing this?

for dragon in dragons:
    if dragon['breed'] not in breeds.keys():
        breeds[dragon['breed']] = dragon


# Grouping by breed
with open('breed_sorted_dragons.csv', 'w') as fhandle:
        for breed in breed_breakdown.keys():
            for dragon in breed_breakdown[breed]:
                fhandle.write(
                    ",".join(value for key, value in dragon.items()) + "\n")


# Grouping by age
age_breakdown = breakdown_by_property(dragons, 'age')

ages = sorted([int(age) for age in age_breakdown.keys()])

with open('age_sorted_dragons.csv', 'w') as fhandle:
    for age in ages:
        for dragon in age_breakdown[str(age)]:
            fhandle.write(
                ",".join(value for key, value in dragon.items()) + "\n")
