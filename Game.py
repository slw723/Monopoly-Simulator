import sys

from Board import Board
from Player import Player


def updatePlayerPropertyGroups(player, property):
    if property.group == "Dark Purple":
        player.numDarkPurple += 1
    elif property.group == "Light Blue":
        player.numLightBlue += 1
    elif property.group == "Pink":
        player.numPink += 1
    elif property.group == "Orange":
        player.numOrange += 1
    elif property.group == "Red":
        player.numRed += 1
    elif property.group == "Yellow":
        player.numYellow += 1
    elif property.group == "Green":
        player.numGreen += 1
    elif property.group == "Dark Blue":
        player.numDarkBlue += 1
    elif property.group == "Utility":
        player.numUtilities += 1
    elif property.group == "Station":
        player.numStations += 1


def evaluateBoardPosition(currentProperty, player, roll, verbosity):
    # if current position is go to jail, move to jail
    if currentProperty.index == 30:
        player.boardPosition = 10
        if verbosity == 3:
            print(f"  Player {player.index} ({player.money}, {currentProperty.name}) goes to jail")

    # if current position is luxury tax, pay $75
    elif currentProperty.index == 38:
        player.money -= 75
        if verbosity == 3:
            print(f"  Player {player.index} ({player.money}, {currentProperty.name}) pays luxury tax")

    # if current position is income tax, pay 10% of total money
    elif currentProperty.index == 4:
        player.money -= round(player.money * 0.1)
        if verbosity == 3:
            print(f"  Player {player.index} ({player.money}, {currentProperty.name}) pays income tax")

    # if current position is Go, collect an additional $200
    elif currentProperty.index == 0:
        player.money += 200  # additional 200 from what the player already gets from passing go
        if verbosity == 3:
            print(f"  Player {player.index} ({player.money}, {currentProperty.name}) lands on Go!")

    # if current position is not a property, continue to next player
    elif not currentProperty.isProperty:
        if verbosity == 3:
            print(f"  Player {player.index} ({player.money}, {currentProperty.name})")
        # continue  # add stuff for cards here

    # if current position is not owned and player can afford the property
    elif (currentProperty.owner == -1 and
          currentProperty.costToBuy <= player.money):
        player.buyProperty(currentProperty.costToBuy)
        updatePlayerPropertyGroups(player, currentProperty)
        player.addProperty(currentProperty.index)
        currentProperty.owner = player
        if verbosity == 3:
            print(f"  Player {player.index} ({player.money}, {currentProperty.name}) now owns {currentProperty.name}!")

    # if current position is owned, player pays the owner (unless the owner is yourself, then do nothing)
    elif currentProperty.owner != -1 and currentProperty.owner != player:
        # Electric Company (12) or Water Works (28)
        if currentProperty.index == 12 or currentProperty.index == 28:
            if currentProperty.owner.numUtilities == 2:
                cost = roll * 10
            else:
                cost = roll * 4

        # One of the railroad stations
        elif currentProperty.index == 5 or currentProperty.index == 15 or currentProperty.index == 25 or currentProperty.index == 35:
            if currentProperty.owner.numStations == 2:
                cost = currentProperty.rentCost * 2
            elif currentProperty.owner.numStations == 3:
                cost = currentProperty.rentCost * 4
            elif currentProperty.owner.numStations == 4:
                cost = currentProperty.rentCost * 8
            else:
                cost = currentProperty.rentCost

        # If the property owner owns all properties in the color group, double rent
        elif currentProperty.owner.ownAllPropertyGroup(currentProperty.index) == 1:
            cost = currentProperty.rentCost * 2

        # Else, rent cost
        else:
            cost = currentProperty.rentCost

        player.payRent(cost)
        currentProperty.owner.getRent(cost)
        if verbosity == 3:
            print(f"  Player {player.index} ({player.money}, {currentProperty.name}) paid Player {currentProperty.owner.index} ${cost}")

    else:
        if verbosity == 3:
            print(f"  Player {player.index} ({player.money}, {currentProperty.name})")


class Game:
    def __init__(self, numPlayers, verbosity):  # add default number of players, put cap on max number of players
        self.numPlayers = numPlayers
        self.board = Board()

        if numPlayers > 8:
            print(f"Number of players entered ({numPlayers}) exceeds the limit (8). Please try again.")
            sys.exit()

        self.players = list()
        self.round = 0
        self.numActive = numPlayers
        self.verbosity = verbosity
        self.numPropertiesOwned = 0

    def createPlayers(self):
        for player in range(self.numPlayers):
            self.players.append(Player(player))

    def startGame(self):
        while self.round < 50:
            if self.numActive == 1:
                print("One player remaining. Game over!")
                break
            if self.verbosity == 3:
                print(f"Current round: {self.round}")
            for player in self.players:
                # if player is inactive, continue to next player
                if player.active == 0:
                    if self.verbosity == 3:
                        print(f"  Player {player.index} is inactive!")
                    continue
                roll = player.move()
                currentProperty = self.board.properties[player.boardPosition]
                evaluateBoardPosition(currentProperty, player, roll, self.verbosity)
                if player.isBankrupt() == 1:
                    self.numActive -= 1
                    for prop in player.properties:
                        self.board.properties[prop].owner = -1
                    if self.verbosity == 3:
                        print(f"  Player {player.index} is now bankrupt!")
            self.round += 1
            if self.verbosity == 3:
                print("")
        for player in self.players:
            if self.verbosity == 3:
                print(f"Player {player.index} ({player.active}) has the following properties:")
            for properties in player.displayProperties():
                self.numPropertiesOwned += 1
                if self.verbosity == 3:
                    print(f"  {self.board.properties[properties].name} ({properties})")

            if self.verbosity == 3:
                print("")

        if self.verbosity == 1:
            self.verbosity_one()

        elif self.verbosity == 2:
            self.verbosity_two()

        else:
            self.verbosity_three()

    # end game summary only
    def verbosity_one(self):
        print("Game Summary")
        print(f"  * Number of Rounds: {self.round}")
        print(f"  * Number of Players: {self.numPlayers}")
        print(f"  * Number of Active Players (after {self.round} rounds): {self.numActive}")
        print(f"  * Number of Owned Properties: {self.numPropertiesOwned}")

    def verbosity_two(self):
        self.verbosity_one()
        print("")

        try:
            print("Owned Property Summary")
            print("=======================================")
            print("| Name                     | Owner    | ")
            print("---------------------------------------")
            print("| Dark Purple              |          |")
            print(f"|  * Mediterranean Avenue  | Player {self.board.properties[1].owner.index} |")
            print(f"|  * Baltic Avenue         | Player {self.board.properties[3].owner.index} |")
            print("---------------------------------------")
            print("| Light Blue               |          |")
            print(f"|  * Oriental Avenue       | Player {self.board.properties[6].owner.index} |")
            print(f"|  * Vermont Avenue        | Player {self.board.properties[8].owner.index} |")
            print(f"|  * Connecticut Avenue    | Player {self.board.properties[9].owner.index} |")
            print("---------------------------------------")
            print("| Pink                     |          |")
            print(f"|  * St. Charles Place     | Player {self.board.properties[11].owner.index} |")
            print(f"|  * States Avenue         | Player {self.board.properties[13].owner.index} |")
            print(f"|  * Virginia Avenue       | Player {self.board.properties[14].owner.index} |")
            print("---------------------------------------")
            print("| Orange                   |          |")
            print(f"|  * St. James Place       | Player {self.board.properties[16].owner.index} |")
            print(f"|  * Tennessee Avenue      | Player {self.board.properties[18].owner.index} |")
            print(f"|  * New York Avenue       | Player {self.board.properties[19].owner.index} |")
            print("---------------------------------------")
            print("| Red                      |          |")
            print(f"|  * Kentucky Avenue       | Player {self.board.properties[21].owner.index} |")
            print(f"|  * Indiana Avenue        | Player {self.board.properties[23].owner.index} |")
            print(f"|  * Illinois Avenue       | Player {self.board.properties[24].owner.index} |")
        except AttributeError:
            print("Error")

    # round by round play of each player
    def verbosity_three(self):
        print("Start of verbosity 3")
