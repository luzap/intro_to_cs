#
# Helper code for Lab 7 (dictionaries)
#

import random

def genkey():
    key = ''
    a = ord('a') # the ASCII character for lowercase a
    n = a + 13   # the ASCII character for lowercase n

    for i in range(3):
        rand = random.randrange(a, n)
        key += chr(rand)
        
    return key

def ishundred(usrdict):
    if len(usrdict) != 100:
        raise AssertionError('Incorrect dictionary length!')
    print("You're okay!")

dragon_color = [
    'black',
    'white',
    'red',
    'blue',
]

dragon_breed = [
    'Antipodean Opaleye',
    'Chinese Fireball',
    'Common Welsh Green',
    'Hebridean Black',
    'Hungarian Horntail',
    'Norwegian Ridgeback',
    'Peruvian Vipertooth',
    'Romanian Longhorn',
    'Swedish Short-Snout',
    'Ukrainian Ironbelly',
]
