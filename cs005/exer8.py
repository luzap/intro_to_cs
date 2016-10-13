"""2.1 Matrix transposition."""

mtx = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [7, 8, 9, 8],
       [10, 11, 12, 13]]

trans_mtx = []
for i in range(len(mtx)):
    trans_mtx.append([0] * len(mtx[0]))

for i in range(len(mtx)):  # Row
    for j in range(len(mtx[0])):   # Column
        trans_mtx[i][j] = mtx[j][i]  # Definition of transpose

print("Original matrix:")
for i in mtx:
    print(i)

print("")

print("Transposed matrix:")
for i in trans_mtx:
    print(i)
