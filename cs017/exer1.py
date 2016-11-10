"""Exercise 1.1: Players."""


class Player:

    def __init__(self, name):
        self.name = name
        self.power = 100

    def __str__(self):
        return self.name + "\t" + str(self.power)


class FastPlayer(Player):

    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def __str__(self):
        return super().__str__() + "\t" + str(self.speed)


class TallPlayer(Player):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def __str__(self):
        return super().__str__() + "\t" + str(self.height)


class CoolPlayer(Player):

    def __init__(self, name, awesomeness):
        super().__init__(name)
        self.awesomeness = awesomeness

    def __str__(self):
        return super().__str__() + "\t" + str(self.awesomeness)

a = Player('Johny')
print(a)
b = TallPlayer("Tim", 1.8)
print(b)
c = FastPlayer("Tom", 5)
print(c)
d = CoolPlayer("Minchin", 0)
print(d)
