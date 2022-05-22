from flask import render_template, request
from app import app
# from models.players import players
from models.player import Player
from models.game import *



@app.route('/home')
def index():
    return render_template("index.html", title= 'Play')



@app.route('/<player1_choice>/<player2_choice>')
def play(player1_choice, player2_choice):
    player1 = Player("Harry", player1_choice)
    player2 = Player("Paddy", player2_choice)
    game = Game()


    winner = game.win_game(player1, player2)
    print(winner)
    return render_template('game.html', title='Play', player1=player1, player2=player2, winner=winner)
