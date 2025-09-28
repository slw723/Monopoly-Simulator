import random


class Player:
    def __init__(self, index):
        self.index = index
        self.money = 500  # need to verify this is correct
        self.boardPosition = 0
        self.properties = list()
        self.active = 1

    def move(self):
        randInt = random.randint(1, 12)
        self.boardPosition += randInt
        if self.boardPosition > 39:
            self.boardPosition = self.boardPosition % 40
            self.money += 200
        # print(f"Player {self.index} is on position {self.boardPosition}")

    def buyProperty(self, cost):
        if cost > self.money:
            print("This property is too expensive!")  # this should never happen
        else:
            self.money -= cost
            # print(f"Player {self.index} now has ${self.money}")

    def addProperty(self, index):
        self.properties.append(index)

    def payRent(self, rent):
        self.money -= rent
        if self.money < 0:
            print(f"Player {self.index} is now bankrupt!")
            self.active = 0

    def getRent(self, rent):
        self.money += rent

    def displayProperties(self):
        print(f"Player {self.index} ({self.active}) has the following properties:")
        for propertyListIndex in self.properties:
            print(f"{propertyListIndex}")
