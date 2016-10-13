"""2.2 Making the band."""

print("Enter coordinates row first (column, row)")
first_coord_text = input("What's the first coordinate?").split(",")
second_coord_text = input("What's the second coord?").split(",")

first_coord = list(map(lambda x: int(x), first_coord_text))
second_coord = list(map(lambda x: int(x), second_coord_text))

crosses = [[" "] * 3, [" "] * 3, [" "] * 3]

# Would need to modify for different sizes of matrices
coordlist = [first_coord, second_coord]
if (second_coord[0] - first_coord[0]) > 1:
    coordlist.insert(1, [int((second_coord[0] - first_coord[0]) / 2),
                         second_coord[1]])

for pair in coordlist:
    crosses[pair[0]][pair[1]] = "x"

print("+" + "-+" * len(crosses[0]))
for i in range(len(crosses)):
    print("|", end="")
    for j in range(len(crosses[0])):
        print(crosses[i][j], end="|")
    print("\n+" + "-+" * len(crosses[0]))
