from tp.exceptions import TooFewPlayers

from tp.deck import Deck
from tp.bank import Bank
from tp.player import Player
from tp.card import *


class TurnMixin(object):
    def next_player(self):
        if self.nump > 0:
            self.current_player = list(self.players)[self.turn_num % len(self.players)]
            self.turn_num += 1


class Game(TurnMixin):
    Max_Players = 5
    Move_PT = 3

    def __init__(self):
        # RULE: max 5 players

        # 1. SET UP
        self.deck = Deck()
        self.players = set([])
        self.current_player = None
        self.turn_num = 0

        # can't add more player after
        self._started = False


    def run(self):
        if len(self.players) >= 1  and not self._started:
            self._started = self._deal_start()

            self.next_player()
        else:
            raise TooFewPlayers()

    def add_player(self, id, name):
        if self.nump < Game.Max_Players and not self._started:
            new_player = Player(id, name)
            new_player.in_game = True
            self.players.add(new_player)
        else:
            raise TooManyPlayers()

    def get_player(self, id, name=""):
        player = [p for p in self.players if p.id == id]
        if len(player) > 0:
            return player[0]

        return None

    def _deal_start(self):
        # RULE:
        #  start of game deal all players 5 cards
        #for i in xrange(len(self.players) * 5):
            #list(self.players)[i % len(self.players)].hand.append(next(self.deck))

        return True

    def _draw(self, count=2):
        # RULE:
        #  draw cards @ beg of turn | use Go | empty hand
        pass

    @property
    def nump(self):
        return len(self.players)

    def is_full(self):
        return self.nump == Game.Max_Players


