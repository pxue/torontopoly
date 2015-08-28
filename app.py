import settings
import time
import ujson
import uuid

from flask import (Flask, flash, make_response, \
        render_template, redirect, request,\
        session, url_for)
from flask.ext.socketio import SocketIO, emit, send, join_room
from flask.ext.login import LoginManager, login_user, current_user

from lib.exception import *
from lib.game import Game
from lib.player import Player

# application
app = Flask(__name__)
app.config.from_object(settings.DevelopmentConfig)

# socketio
#TODO: centrifugal? http://fzambia.gitbooks.io/centrifugal/
socketio = SocketIO(app)

# login manager
login_manager = LoginManager(app)


# globals
game = Game()

@socketio.on("add_bank", namespace="/game")
def on_add_bank(idx):

    # add card to bank
    card = current_user.hand.pop(int(idx))
    current_user._bank.add(card)

    # data on current players
    emit("players", ujson.dumps([{
            "name": p.name,
            "money": p.money,
            "cards": len(p.hand)
        } for p in game.players]), json=True, broadcast=True)


@socketio.on("user_connected", namespace="/game")
def on_user_connected(message):
    if not current_user.is_anonymous():
        send("{0} has connected".format(current_user.name))
        join_room(current_user.id) # user's own channel

        # data on current players
        emit("players", ujson.dumps([{
                "name": p.name,
                "money": p.money,
                "cards": len(p.hand)
            } for p in game.players]), json=True, broadcast=True)
        
        if game._started and current_user.in_game:
            emit("player_hand", ujson.dumps(current_user.hand), json=True,
                    room=current_user.id)


@socketio.on("message", namespace="/game")
def on_message(message):
    if message["data"][0] == "/":
        command = message["data"][1:]
        if command == "start":
            game.run()
            send("{0} has started the game".format(current_user.name),
                    broadcast=True)

            # show each player their hands
            for token in socketio.rooms["/game"].keys():
                hand = ujson.dumps(game.get_player(token).hand)
                emit("player_hand", hand, json=True, room=token)

        # update player box with current data
        emit("players", ujson.dumps([{
                "name": p.name,
                "money": p.money,
                "cards": len(p.hand)
            } for p in game.players]), json=True, broadcast=True)

    else:
        send("{0}: {1}".format(current_user.name, message["data"]), broadcast=True)


@app.route("/")
def index():
    if current_user.is_anonymous():
        resp = make_response(render_template("login.html"))
        resp.set_cookie("token", str(uuid.uuid4()))
    else:
        resp = make_response(render_template("index.html"))

    #resp = make_response(render_template("index.html"))

    return resp


@app.route("/session", methods=["POST"])
def session():
    #TODO: fblogin
    name = request.form.get("name", "Player%d" % (len(game.players) + 1))
    token = request.cookies.get("token")

    if not game.get_player(token):
        try:
            player = Player(token, name)
            game.add_player(player)
            login_user(player, True) # log the guy in
        except TooManyPlayers:
            flash("too many players!")

    return redirect(url_for("index"))

@login_manager.user_loader
def load_player(token):
    if game == None:
        return None
    return game.get_player(token)


if __name__ == "__main__":
    socketio.run(app)
