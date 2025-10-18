class Property:
    def __init__(self, index, name, costToBuy, isProperty, rentCost, group):
        self.index = index
        self.name = name
        self.costToBuy = costToBuy
        self.isProperty = isProperty
        self.rentCost = rentCost
        self.owner = -1
        self.group = group

    def getName(self, index):
        return self.name

