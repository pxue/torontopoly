
class TooManyPlayers(Exception):
    def __init__(self, num):
        super(Exception, self).__init__("%d is too many players." % num)

class TooFewPlayers(Exception):
    def __init__(self):
        super(Exception, self).__init__("not enough players to start the game.")
