from Board import Board
from Player import Player


class Game:
    board = Board()
    players = list()
    round = 0

    def __init__(self, numPlayers):  # add default number of players
        self.numPlayers = numPlayers

    def createPlayers(self):
        for player in range(self.numPlayers):
            self.players.append(Player(player))

    def startGame(self):
        while self.round < 10:
            print(f"Current round: {self.round}")
            for player in self.players:
                player.move()
                currentProperty = self.board.properties[player.boardPosition]
                if not currentProperty.isProperty:
                    continue  # add stuff for cards here

                if (currentProperty.owner == -1 and
                        currentProperty.costToBuy <= player.money):
                    player.buyProperty(currentProperty.costToBuy)
                    player.addProperty(currentProperty.index)
                    currentProperty.owner = player.index
                    print(f"Player {player.index} now has {currentProperty.name}!")
            self.round += 1
        for player in self.players:
            player.displayProperties()


