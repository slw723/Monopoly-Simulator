from Board import Board
from Player import Player


class Game:
    board = Board()
    players = list()

    def __init__(self, numPlayers):
        self.numPlayers = numPlayers

    def createPlayers(self):
        for player in self.numPlayers:
            self.players.append(Player(player))


game1 = Game(5)
print(game1.board.properties[5].name)
