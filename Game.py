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
        while self.round < 20:
            if self.numActive == 1:
                print("One player remaining. Game over!")
                break
            print(f"Current round: {self.round}")
            for player in self.players:
                # if player is inactive, continue to next player
                if player.active == 0:
                    print(f"Player {player.index} is inactive!")
                    continue
                player.move()
                currentProperty = self.board.properties[player.boardPosition]
                # if current position is go to jail, move to jail
                if currentProperty.index == 30:
                    player.boardPosition = 10
                    print(f"Player {player.index} ({player.money}, {currentProperty.name}) goes to jail")

                # if current position is not a property, continue to next player
                elif not currentProperty.isProperty:
                    print(f"Player {player.index} ({player.money}, {currentProperty.name})")
                    continue  # add stuff for cards here

                # if current position is not owned and player can afford the property
                elif (currentProperty.owner == -1 and
                        currentProperty.costToBuy <= player.money):
                    player.buyProperty(currentProperty.costToBuy)
                    player.addProperty(currentProperty.index)
                    currentProperty.owner = player.index
                    print(f"Player {player.index} ({player.money}, {currentProperty.name}) now owns {currentProperty.name}!")

                # if current position is owned, player pays the owner
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


