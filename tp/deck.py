import ujson
from random import shuffle

from tp.card import *
# deck object

class Deck(object):
    MONEY = { 10: 1, 5: 2, 4: 3, 3: 3, 2: 5, 1: 6, }

    def __init__(self):
        self.deck = []

        for val, count in Deck.MONEY.iteritems():
            self._money = [MoneyCard(val) for _ in xrange(count)]
            self.deck += self._money

        with open("fixtures/properties.json", "r") as f:
            self._properties = [PropertyCard(**p) for p in ujson.loads(f.read())]
            self.deck += self._properties

        with open("fixtures/double_properties.json", "r") as f:
            self._double_properties = [DoublePropertyCard(**p) for p in ujson.loads(f.read())]
            self.deck += self._double_properties

        self._wild_properties = [WildPropertyCard() for _ in xrange(2)]
        self.deck += self._wild_properties

        with open("fixtures/rents.json", "r") as f:
            self._rent = [RentCard(**p) for p in ujson.loads(f.read())]
            self.deck += self._rent

        self._wild_rent = [WildRentCard() for _ in xrange(3)]
        self.deck += self._wild_rent

        with open("fixtures/actions.json", "r") as f:
            self._action = []
            for p in ujson.loads(f.read()):
                self._action += [ActionCard(**p) for _ in xrange(p["count"])]
            self.deck += self._action

        # shuffle 5 times
        [shuffle(self.deck) for _ in xrange(5)]

    def __iter__(self):
        return self

    def next(self):
        if len(self.deck) == 0:
            # TODO: reshuffle discard pile
            raise StopIteration
        else:
            return self.deck.pop()
