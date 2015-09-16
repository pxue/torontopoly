
# player's bank
class Bank(object):
    def __init__(self, player):
        self.player = player
        self.bank = []

    def add(self, card):
        self.bank.append(card)

    # let player remove from bank
    # TODO: greedy algorithm to determine
        # best combo to remove
    def remove(self, index):
        del self.bank[index]

    def list(self):
        return self.bank

    def sum(self):
        return sum([m.value for m in self.bank])
