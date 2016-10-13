"""Exercise 1.3: Sub-list products."""
import random

list_of_lists = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12]]


def product_array(md_array):
    """Return a list of products."""
    products = [1] * len(md_array)

    for list in md_array:
        list_index = md_array.index(list)
        for item in list:
            products[list_index] *= item

    return products


print("Products of the rows of a given 4*3 array:",
      product_array(list_of_lists))


# Random m*n array
columns = 10
rows = 10

deep_list = []
temp_list = []

for i in range(rows):
    for j in range(columns):
        temp_list.append(random.uniform(1, 20))
    deep_list.append(temp_list)
    temp_list = []

print("Products of the rows of a random array:", product_array(deep_list))
