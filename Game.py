from Board import Board
from Player import Player


class Game:
    def __init__(self, numPlayers):  # add default number of players, put cap on max number of players
        self.numPlayers = numPlayers
        self.board = Board()
        self.players = list()
        self.round = 0
        self.numActive = numPlayers

    def createPlayers(self):
        for player in range(self.numPlayers):
            self.players.append(Player(player))

    def startGame(self):
        while self.round < 30:
            if self.numActive == 1:
                print("One player remaining. Game over!")
                break
            print(f"Current round: {self.round}")
            for player in self.players:
                if player.active == 0:
                    print(f"Player {player.index} is inactive!")
                    continue
                player.move()
                currentProperty = self.board.properties[player.boardPosition]
                if not currentProperty.isProperty:
                    print(f"Player {player.index} ({player.money}, {currentProperty.name})")
                    continue  # add stuff for cards here

                elif (currentProperty.owner == -1 and
                        currentProperty.costToBuy <= player.money):
                    player.buyProperty(currentProperty.costToBuy)
                    player.addProperty(currentProperty.index)
                    currentProperty.owner = player.index
                    print(f"Player {player.index} ({player.money}, {currentProperty.name}) now owns {currentProperty.name}!")

                elif currentProperty.owner != -1:
                    player.payRent(currentProperty.rentCost)
                    self.players[currentProperty.owner].getRent(currentProperty.rentCost)
                    print(f"Player {player.index} ({player.money}, {currentProperty.name}) paid Player {currentProperty.owner} ${currentProperty.rentCost}")

                else:
                    print(f"Player {player.index} ({player.money}, {currentProperty.name})")

            self.round += 1
            print("")
        for player in self.players:
            player.displayProperties()


