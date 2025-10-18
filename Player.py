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

    def sellProperty(self, index):
        self.properties.remove(index)

    def isBankrupt(self):
        if self.money <= 0:
            self.active = 0
            for prop in self.properties:
                self.sellProperty(prop)
            return 1
        else:
            return 0

    def displayProperties(self):
        print(f"Player {self.index} ({self.active}) has the following properties:")
        return self.properties

    def ownAllPropertyGroup(self, index):
        if (index == 1 or index == 3) and (self.numDarkPurple == 2):
            return 1
        elif (index == 6 or index == 8 or index == 9) and (self.numLightBlue == 3):
            return 1
        elif (index == 11 or index == 13 or index == 14) and (self.numPink == 3):
            return 1
        elif (index == 16 or index == 18 or index == 19) and (self.numOrange == 3):
            return 1
        elif (index == 21 or index == 23 or index == 24) and (self.numRed == 3):
            return 1
        elif (index == 26 or index == 27 or index == 29) and (self.numYellow == 3):
            return 1
        elif (index == 31 or index == 32 or index == 34) and (self.numGreen == 3):
            return 1
        elif (index == 37 or index == 39) and (self.numDarkBlue == 2):
            return 1
        else:
            return 0
