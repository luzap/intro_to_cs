import random
from collections import OrderedDict

import lab

tests = 10
possibles = ['FAIL', 'PASS']
results = OrderedDict()

#
# Exponentiate
#
x = True
for i in range(3):
    for j in range(0, 10, 2):
        x &= i ** j == lab.exponentiate(i, j)
results['exponentiate'] = x

#
# get_nth
#
x = True
for i in range(3):
    rlist = random.sample(range(2 ** 10), 100)
    for j in range(tests):
        item = random.randrange(len(rlist))
        x &= rlist[item] == lab.get_nth(rlist, item)
results['get_nth'] = x

#
# reverse
#
x = True
for i in range(3):
    rlist = random.sample(range(2 ** 10), 100)
    for j in range(tests):
        x &= rlist[::-1] == lab.reverse(rlist)
results['reverse'] = x

#
# is_older
#
x = True
for _ in range(tests):
    year = random.randint(1900, 2020)
    month = random.randint(1, 12)
    day = random.randint(10, 20)
    today = [ year, month, day ]

    for (i, j) in enumerate(today):
        another_day = today.copy()
        for k in range(-1, 2):
            another_day[i] = j + k
            print(today, another_day, lab.is_older(today, another_day))
            x &= not lab.is_older(today, another_day) ^ (k > 0)
results['is_older'] = x

#
# number_before_reaching_sum
#
if hasattr(lab, 'number_before_reaching_sum'):
    x = lab.number_before_reaching_sum(10, list(range(1, 6))) == 3
    results['number_before_reaching_sum'] = x

#
# what_month
#
if hasattr(lab, 'what_month'):
    x = lab.what_month(70) == 3
    results['what_month'] = x

for (i, j) in results.items():
    print(possibles[j], i)
