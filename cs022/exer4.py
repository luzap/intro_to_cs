"""Exercise 1.4: scatter plot."""
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

colorize = {
    'Male': {'Yes': 'r', 'No': 'b'},
    'Female': {'Yes': 'y', 'No': 'g'}
}


bill = list(map(float, data['total_bill']))
tips = list(map(float, data['tip']))
smokers = data['smoker']
genders = data['sex']

color = []
for i in range(len(smokers)):
    color.append(colorize[genders[i]][smokers[i]])

plt.scatter(bill, tips, c=color)
plt.xlabel("Bill")
plt.ylabel("Tip")
plt.show()
