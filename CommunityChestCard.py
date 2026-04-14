import random


def advanceToGo(player):
    player.boardPosition = 0
    player.money += 200


def bankError(player):
    player.money += 200


def doctorsFee(player):
    player.money -= 50


def saleOfStock(player):
    player.money += 50


def getOutOfJail(player):
    player.getOutOfJail = 1


def goToJail(player):
    player.boardPosition = 10
    player.inJail = 1


def holidayFund(player):
    player.money += 100


def taxRefund(player):
    player.money += 20


# def birthday(player, game):
#     for allPlayers in game.players:
#         if allPlayers.active == 0:
#             continue
#         elif allPlayers.index == player.index:
#             continue
#         else:
#             allPlayers.money -= 10
#             player.money += 10


def lifeInsurance(player):
    player.money += 100


def hospitalFee(player):
    player.money -= 100


def schoolFee(player):
    player.money -= 50


def consultFee(player):
    player.money += 25


def houseHotel(player):
    # needs to be updated once house/hotel build is complete
    player.money += 0


def beautyContest(player):
    player.money += 10


def inherit(player):
    player.money += 100


class CommunityChestCard:
    def __init__(self, index, name):
        self.index = index
        self.name = name

    def getCommunityChestAction(self, player):
        cardIndex = random.randint(0, 15)

        if cardIndex == 0:
            advanceToGo(player)
        elif cardIndex == 1:
            bankError(player)
        elif cardIndex == 2:
            doctorsFee(player)
        elif cardIndex == 3:
            saleOfStock(player)
        elif cardIndex == 4:
            getOutOfJail(player)
        elif cardIndex == 5:
            goToJail(player)
        elif cardIndex == 6:
            holidayFund(player)
        elif cardIndex == 7:
            taxRefund(player)
        # elif cardIndex == 8:
        #     birthday(player, game)
        elif cardIndex == 9:
            lifeInsurance(player)
        elif cardIndex == 10:
            hospitalFee(player)
        elif cardIndex == 11:
            schoolFee(player)
        elif cardIndex == 12:
            consultFee(player)
        elif cardIndex == 13:
            houseHotel(player)
        elif cardIndex == 14:
            beautyContest(player)
        elif cardIndex == 15:
            inherit(player)
