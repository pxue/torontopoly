CARD_MONEY = 1
CARD_PROPERTY = 2
CARD_ACTION = 3
CARD_RENT = 4
CARD_DOUBLEP = 5
CARD_WILDP = 6
CARD_WILDR = 7

PROPERTY_RENT = {
    "blue": [3, 7],
    "green": [2, 4, 7],
    "brown": [1, 2],
    "lightblue": [1, 2, 3],
    "orange": [1, 3, 5],
    "pink": [1, 2, 4],
    "rail": [1, 2, 3, 4],
    "red": [2, 3, 6],
    "util": [1, 2],
    "yellow": [2, 4, 6]
}

PROPERTY_COLOUR = {
    "blue": "#4E86DF",
    "orange": "#ECB175",
    "green": "#167C00",
    "brown": "#7A3D37",
    "lightblue": "#96BCDE",
    "pink": "#B538A6",
    "rail": "black",
    "red": "#D1262B",
    "util": "#B8C1C0",
    "yellow": "#D5DD3B",
}

# object representing an hightlevel card
class Card(object):

    def __init__(self, type, value, name=""):
        self.type = type
        self.value = value
        self.name = name

    def use(self):
        raise Exception("Must implement.")

    def __repr__(self):
        return self.name

class MoneyCard(Card):
    def __init__(self, value):
        Card.__init__(
            self,
            CARD_MONEY,
            value,
            "|Money: %d|" % value
        )


class PropertyCard(Card):
    def __init__(self, value, colour, name):
        Card.__init__(self, CARD_PROPERTY, value, name)

        self.colour = colour
        self.colour_code = PROPERTY_COLOUR[self.colour]
        self.rent = PROPERTY_RENT[colour]


class DoublePropertyCard(Card):
    def __init__(self, value, name, primary, secondary):
        name = "|DoubleProperty: %s/%s|" % (primary, secondary)
        Card.__init__(self, CARD_DOUBLEP, value, name)

        self.primary = primary
        self.primary_rent = PROPERTY_RENT[primary]
        self.secondary = secondary
        self.secondary_rent = PROPERTY_RENT[secondary]


class WildPropertyCard(Card):
    def __init__(self):
        name = "|WildProperty|"
        Card.__init__(self, CARD_WILDP, 0, name)


class ActionCard(Card):
    def __init__(self, **kwargs):
        Card.__init__(self, CARD_ACTION, kwargs["value"], kwargs["name"])

        self.description = kwargs["desc"]


class RentCard(Card):
    def __init__(self, value, primary, secondary):
        name = "|Rent: %s/%s|" % (primary, secondary)
        Card.__init__(self, CARD_RENT, value, name)
        self.primary = primary
        self.secondary = secondary


class WildRentCard(RentCard):
    def __init__(self):
        name = "|WildRent|"
        Card.__init__(self, CARD_WILDR, 3, name)
