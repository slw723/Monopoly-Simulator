from Board import Board
from Player import Player


class Game:
    board = Board()
    players = list()

    def __init__(self, numPlayers):  # add default number of players
        self.numPlayers = numPlayers

    def createPlayers(self):
        for player in range(self.numPlayers):
            self.players.append(Player(player))


testGame = Game(3)
testGame.createPlayers()
# print(len(testGame.players))
testGame.players[0].move()
testGame.players[1].move()
print(testGame.players[0].boardPosition)
