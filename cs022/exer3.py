"""Exercise 1.3: contribution pie chart."""
import csv
from collections import OrderedDict

import numpy as np
import matplotlib.pyplot as plt


def get_data_dict(file):
    with open(file) as fhandle:
        # Make dictionary reader
        reader = csv.DictReader(fhandle)

        # Order the dictionaries, thereby bypassing the need to
        # make sure the keys are still the same
        data = OrderedDict()

        for row in reader:
            for key in row.keys():
                if key not in data:
                    data[key] = []
                data[key].append(row[key].strip())
        return data

data = get_data_dict('tips.csv')

columns = list(zip(data['day'], map(
    float, data['total_bill'])))

total = {}

for row in columns:
    if row[0] not in total:
        total[row[0]] = []
    total[row[0]].append(row[1])

for day in total:
    total[day] = sum(total[day])

plt.pie(list(total.values()), autopct='%1.1f%%', labels=total.keys())
plt.axis('equal')

plt.show()
