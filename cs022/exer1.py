"""Exercise 1: Plotting with data."""
import csv
import operator
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
    float, data['total_bill']), map(float, data['tip'])))

total = OrderedDict()
tips = OrderedDict()

for row in columns:
    if row[0] not in total:
        total[row[0]] = []
    total[row[0]].append(row[1])

    if row[0] not in tips:
        tips[row[0]] = []
    tips[row[0]].append(row[2])


total = {key: round(np.mean(value), 2) for key, value in total.items()}
tips = {key: round(np.mean(value), 2) for key, value in tips.items()}

width = 0.25

locs = np.arange(len(total)) + 1
tot = plt.bar(locs, total.values(), width, color='r', )
tips = plt.bar(locs, tips.values(), width, color='b', bottom=total.values())

plt.xlabel("Day")
plt.ylabel("Average amount")
plt.legend((tot[0], tips[0]), ("Total", "Tips"), loc='best')

plt.xticks(locs + width / 2, total.keys())
plt.show()
