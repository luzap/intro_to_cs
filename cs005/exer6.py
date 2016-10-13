"""1.6 Age commentary."""

age = int(input("What's your age? ").strip())

if 120 < age < 0:
    print("Are you really now?")
elif 40 >= age >= 0:
    print("Sounds about right.")
elif 100 > age >= 40:
    print("Did not expect such an audience.")
else:
    print("Hmm, you sure about that?")
