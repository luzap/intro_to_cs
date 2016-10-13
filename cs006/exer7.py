"""Exercise 2.2: Create your own replace."""
source = 'Adam made him take a placard'
s1 = 'a'
s2 = 'z'
target = []

# 1.1 Replacement of character (case-insensitive)
source_list = list(source)
for item in source_list:
    if item == s1:
        target.append(s2)
    else:
        target.append(item)


print("Replacement ignoring case:", "".join(target))

# 1.2 Replacement of character (case-insensitive)
target = []
for item in source_list:
    if item == s1.upper():
        target.append(s2.upper())
    elif item == s1.lower():
        target.append(s2.lower())
    else:
        target.append(item)

print("Replacement with case:", "".join(target))

# 1.3 User input
source = input("Your string: ")
s1 = input("Unwanted character: ")
s2 = input("Replacement character: ")

target = []
for item in list(source):
    if item == s1.upper():
        target.append(s2.upper())
    elif item == s1.lower():
        target.append(s2.lower())
    else:
        target.append(item)

print("User specific string: ", "".join(target))

# 1.4 User input with multiple replacement characters
source = input("Your input: ")
uchars = list(input("Unwanted character(s): "))
s2 = input("Replacement character: ")

target = []
for uchar in uchars:
    for item in list(source):
        if item == uchar.upper():
            target.append(s2.upper())
        elif item == uchar.lower():
            target.append(s2.lower())
        else:
            target.append(item)
    source = "".join(target)
    target = []

print("User input with multiple char replacement:", source)

# Extra - the needlessly complicated way


class ModString(str):

    def __init__(self, text):
        super().__init__()
        self.text = text

    def replace(self, old, new, count=None):
        target = []
        uchars = list(old)
        for uchar in uchars:
            for item in list(self.text):
                if item == uchar.upper():
                    target.append(new.upper())
                elif item == uchar.lower():
                    target.append(new.lower())
                else:
                    target.append(item)
            self.text = "".join(target)
            target = []

        return self.text


trial = ModString("hello")  # Any way of overriding the default type assignment
trial_2 = trial.replace("e", "l")
print("Replacement via class overriding:", trial_2)
