import random


class Player:
    money = 500  # need to verify this is correct
    boardPosition = 0
    properties = list()

    def __init__(self, index):
        self.index = index

    def move(self):
        randInt = random.randint(1, 12)
        self.boardPosition += randInt
        self.boardPosition = self.boardPosition % 40
        print(f"Player {self.index} is on position {self.boardPosition}")

    def buyProperty(self, cost):
        if cost > self.money:
            print("This property too expensive!")
        else:
            self.money -= cost
            print(f"Player {self.index} now has ${self.money}")

    def addProperty(self, index):
        self.properties.append(index)

    def displayProperties(self):  # issues with this! displaying same properties for every player... yikes!
        print(f"Player {self.index} has the following properties:")
        for propertyListIndex in self.properties:
            print(f"{propertyListIndex}")
