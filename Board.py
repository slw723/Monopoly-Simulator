from Property import Property


class Board:
    properties = list()

    properties.append(Property(0, "Go", 0))
    properties.append(Property(1, "Mediterranean Avenue", 60))
    properties.append(Property(2, "Community Chest", 0))
    properties.append(Property(3, "Baltic Avenue", 60))
    properties.append(Property(4, "Income Tax", 0))
    properties.append(Property(5, "Reading Railroad", 200))
    properties.append(Property(6, "Oriental Avenue", 100))
    properties.append(Property(7, "Chance", 0))
    properties.append(Property(8, "Vermont Avenue", 100))
    properties.append(Property(9, "Connecticut Avenue", 120))

    properties.append(Property(10, "Just Visiting/Jail", 0))
    properties.append(Property(11, "St. Charles Place", 140))
    properties.append(Property(12, "Electric Company", 150))
    properties.append(Property(13, "States Avenue", 140))
    properties.append(Property(14, "Virginia Avenue", 160))
    properties.append(Property(15, "Pennsylvania Railroad", 200))
    properties.append(Property(16, "St. James Place", 180))
    properties.append(Property(17, "Community Chest", 0))
    properties.append(Property(18, "Tennessee Avenue", 180))
    properties.append(Property(19, "New York Avenue", 200))

    properties.append(Property(20, "Free Parking", 0))
    properties.append(Property(21, "Kentucky Avenue", 220))
    properties.append(Property(22, "Chance", 0))
    properties.append(Property(23, "Indiana Avenue", 220))
    properties.append(Property(24, "Illinois Avenue", 240))
    properties.append(Property(25, "B. & O. Railroad", 200))
    properties.append(Property(26, "Atlantic Avenue", 260))
    properties.append(Property(27, "Ventnor Avenue", 260))
    properties.append(Property(28, "Water Works", 150))
    properties.append(Property(29, "Marvin Gardens", 280))

    properties.append(Property(30, "Go to Jail", 0))
    properties.append(Property(31, "Pacific Avenue", 300))
    properties.append(Property(32, "North Carolina Avenue", 300))
    properties.append(Property(33, "Community Chest", 0))
    properties.append(Property(34, "Pennsylvania Avenue", 320))
    properties.append(Property(35, "Short Line", 200))
    properties.append(Property(36, "Chance", 0))
    properties.append(Property(37, "Park Place", 350))
    properties.append(Property(38, "Luxury Tax", 0))
    properties.append(Property(39, "Boardwalk", 400))


board1 = Board()
print(board1.properties[0].name)
print(len(board1.properties))
