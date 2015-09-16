from tp.bank import Bank

# this is a player

class Player(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.in_game = False

        self._hand = []
        self._bank = Bank(self)
    
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    # this is player's hand
    @property
    def hand(self):
        # RULE:
        #  1. max 7 cards or discard
        if len(self._hand) > 7:
            # TODO: prompt discard
            pass

        return self._hand

    @property
    def money(self):
        # sum of money player have
        return self._bank.sum()

    def __repr__(self):
        return "<Player: %s>" % self.name
