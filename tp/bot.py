import rx
import time
import ujson

from rx import Observable, Observer
from slackclient import SlackClient

from tp.exceptions import TooFewPlayers
from tp.game import Game

class Bot(object):
    # slacker bot

    def __init__(self, token):
        self.token = token
        self._client = None

        self.channel = None
        self.isWaitingPlayer = False
        self.game = None

    def connect(self):
        self._client = SlackClient(self.token)
        return self._client.rtm_connect()

    def start(self):
        self.connect()
        self.id = self._client.server.login_data["self"]["id"]

        self._monitor()

    def isMentioned(self, msg):
        if msg.get("type", "") != "message":
            return False

        if not msg.get("text"):
            return False

        return "@%s" % self.id in msg.get("text")

    # monitor incoming messages
    def _monitor(self):
        while True:
            for reply in self._client.rtm_read():
                if not self.isMentioned(reply):
                    continue

                if self.channel and reply["channel"] != self.channel:
                    continue

                if "deal" in reply["text"]:
                    self.channel = reply["channel"]
                    self._readyStartGame()
                elif ("yes" in reply["text"]) and self.game:
                    if self.game.is_full():
                        self.messages("game is full!")
                        continue #TODO: cancel countdown

                    player_info = ujson.loads(self._client.api_call("users.info", user=reply["user"]))
                    if player_info["ok"]:
                        name = player_info["user"]["name"]
                        self.game.add_player(reply["user"], name)
                        self.message("player <@%s> joined the game.", reply["user"])
                    else:
                        self.message("player failed to join.")
                elif ("cancel" in reply["text"]) and self.game and self.game._started:
                    self.game = None
                else:
                    pass

                print reply
            time.sleep(.1)

    # ready to start the game
    def _readyStartGame(self):
        if self.game is None:
            self.game = Game()

        if self.isWaitingPlayer:
            return self.message("waiting for players.")

        if self.game and self.game._started:
            return self.message("Another game is in already progress.")

        return self._pollPlayers()

    # ask players to join the game
    def _pollPlayers(self, timeout=5, maxPlayers=5):
        self.isWaitingPlayer = True

        def _finish():
            self.isWaitingPlayer = False

            try:
                self.game.run()
            except TooFewPlayers:
                self.message("Not enough players for a game, try again later.")
                return

            self.message("We've got %d players, let's start the game.", self.game.nump)
        
        formatMsg = "Who want's to play? Respond `yes` in this channel in the next %d seconds."

                #filter(lambda t: not t % 10).\
        Observable.interval(1000).\
                take(timeout + 1).\
                subscribe(lambda t: self.message(formatMsg, timeout - t), None, _finish)


    def message(self, msg, *args):
        self._client.rtm_send_message(self.channel, msg % args)
