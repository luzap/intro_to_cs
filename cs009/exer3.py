"""Exercise 1.3: Read a board from a file."""

file = "memory.txt"


def print_md(md_array):
    for item in md_array:
        print("+" + "-+" * len(item))
        print("|" + "|".join(item) + "|")
    print("+" + "-+" * len(md_array[0]))


with open(file, "r+") as fhandle:
    file_text = fhandle.read().split("\n")[:-1]

md_array = []
for line in file_text:
    md_array.append(list(line))

print_md(md_array)


while True:
    s_change_coords = input("What letter would you like to change? ")
    if s_change_coords != "stop":
        change_coords = [int(x) for x in s_change_coords.split(",")]

        letter = input("What do you want it to be changed to? ")
        md_array[change_coords[0]][change_coords[1]] = letter
        print_md(md_array)
    else:
        break

with open(file, "w") as fhandle:
    for row in md_array:
        fhandle.write("".join(row) + "\n")

print("Writing done!")
