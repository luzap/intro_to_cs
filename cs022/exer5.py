"""Exercise 1.5: box plot."""
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

columns = list(zip(data['day'], map(float, data['tip'])))
tips = OrderedDict()

for row in columns:
    if row[0] not in tips:
        tips[row[0]] = []
    tips[row[0]].append(row[1])

plt.boxplot(list(tips.values()))
plt.ylim(ymin=0)
plt.yticks(list(range(10)))
plt.xticks(range(1, 5), list(tips.keys()))
plt.grid(True)
plt.show()
