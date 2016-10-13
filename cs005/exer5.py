"""1.5 Pretty printing."""

list_of_lists = [['a', 'b', 'c'],
                 ['d', 'e', 'f'],
                 ['g', 'h', 'i'],
                 ['a', 'b', 'c'],
                 ['d', 'e', 'f'],
                 ['g', 'h', 'i'],
                 ['a', 'b', 'c'],
                 ['d', 'e', 'f']]

for list in list_of_lists:
    print("+" + "-+" * len(list_of_lists[1]))
    print("|", end="")
    for item in list:
        print(item, end="|")
    print("")
print("+" + "-+" * len(list_of_lists[1]))
