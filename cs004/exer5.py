# Exercise 2.2: String rotation
import timeit

shift = 3

compass = "NESW"
new_compass = []
default_time_loop = timeit.default_timer()

for i in range(shift):
    for j in range(-1, len(compass) - 1):
        new_compass.append(compass[j])
    compass = "".join(new_compass)
    new_compass = []

print("For loop:", timeit.default_timer() - default_time_loop)
print("Shifted:", "".join(compass))

# String rotation via string manipulation
compass = "NESW"
new_compass = ""
default_time_string = timeit.default_timer()

new_compass = compass[len(compass) - shift:] + compass[:len(compass) - shift]
print("String operation:", timeit.default_timer() - default_time_string)
print("Shifted:", new_compass)
