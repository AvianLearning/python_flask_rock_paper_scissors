from app import app
from flask import render_template, request, redirect
from app.models.player import *
from app.models.game import *
from random import choice

@app.route('/')
def index():
    return render_template('play.html', title='Rock, paper, scissors')

@app.route('/<player_1_choice>/<player_2_choice>')
def play(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game = Game(player_1, player_2)
    winner = game.find_winner(player_1, player_2)
    if winner == player_1:
        result = f"{player_1.name} wins by playing {player_1_choice}"
    elif winner == player_2:
        result = f"{player_2.name} wins by playing {player_2_choice}"
    else:
        result = "It's a draw!"
    return render_template('index.html', result=result)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/play', methods=['POST'])
def play_vs_computer():
    player_name = request.form['name']
    player_choice = request.form['choice']
    player_1 = Player(player_name, player_choice)

    weapon_list = ["rock", "paper", "scissors"]
    computer_choice = choice(weapon_list)

    computer = Player("Computer", computer_choice)
    game = Game(player_1, computer)
    winner = game.find_winner(player_1, computer)
    if winner == player_1:
        result = f"{player_1.name} wins by playing {player_choice}. \n Computer chose {computer_choice}."
    elif winner == computer:
        result = f"{computer.name} wins by playing {computer_choice}."
    else:
        result = "It's a draw!"
    return render_template('index.html', result=result)
    









