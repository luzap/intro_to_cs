"""Exercise 1.1: Bank values."""
import random

bank_balance_m = [random.randint(1, 10) for i in range(10)]
bank_balance_f = [random.randint(1, 10) for i in range(10)]

m_good_months = 0
f_good_months = 0  # Compare every value to every other value

for i in range(len(bank_balance_f)):
    if bank_balance_f[i] > bank_balance_m[i]:
        f_good_months += 1
    elif bank_balance_f[i] < bank_balance_m[i]:
        m_good_months += 1

if m_good_months > f_good_months:
    print("He had more prosperous months.")
else:
    print("She had more prosperous months.")
