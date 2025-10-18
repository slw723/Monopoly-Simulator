import random
from Property import Property


class Player:
    numDarkPurple = 0
    numLightBlue = 0
    numPink = 0
    numOrange = 0
    numRed = 0
    numYellow = 0
    numGreen = 0
    numDarkBlue = 0
    numStations = 0
    numUtilities = 0

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
        return randInt

    def buyProperty(self, cost):
        if cost > self.money:
            print("This property is too expensive!")  # this should never happen
        else:
            self.money -= cost

    def addProperty(self, index):
        self.properties.append(index)

    def payRent(self, rent):
        self.money -= rent

    def getRent(self, rent):
        self.money += rent

    def isBankrupt(self):
        if self.money <= 0:
            self.active = 0
            return 1
        else:
            return 0

    def displayProperties(self):
        print(f"Player {self.index} ({self.active}) has the following properties:")
        return self.properties
