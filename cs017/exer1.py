"""Exercise 1.1: Players."""


class Player:

    def __init__(self, name):
        self.name = name
        self.power = 100

    def player_info(self):
        print(self.name)


class FastPlayer(Player):

    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def player_info(self):
        super().player_info()
        print(self.speed)


class TallPlayer(Player):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def player_info(self):
        super().player_info()
        print(self.height)


class CoolPlayer(Player):

    def __init__(self, name, awesomeness):
        super().__init__(name)
        self.awesomeness = awesomeness

    def player_info(self):
        super().player_info(),
        print(self.awesomeness)


a = Player('Johny')
a.player_info()
b = TallPlayer("Tim", 1.8)
b.player_info()
c = FastPlayer("Tom", 5)
c.player_info()
