import random


class Player:
    money = 500  # need to verify this is correct
    boardPosition = 0

    def __init__(self, index):
        self.index = index

    def move(self):
        randInt = random.randint(1, 12)
        # print(randInt)
        self.boardPosition += randInt
        print(self.boardPosition)
