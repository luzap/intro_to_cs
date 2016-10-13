"""Exercise 1.3: Creation and inversion."""
import random

import labhelpers

usrdict = {}
while len(usrdict.keys()) != 100:
    usrdict[labhelpers.genkey()] = 0

for key in usrdict.keys():
    usrdict[key] = random.randint(0, 10)

print(usrdict)
labhelpers.ishundred(usrdict)

inverted_usr_dict = {}
for key, value in usrdict.items():
    if value in inverted_usr_dict.keys():
        inverted_usr_dict[value].append(key)
    else:
        inverted_usr_dict[value] = [key]

print(inverted_usr_dict)
