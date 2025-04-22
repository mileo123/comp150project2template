from flask import Flask, render_template, request, redirect, url_for
import random
import time
from game import fight, start_game_logic, creatures, characters, powers, health, inventory  # Import your game logic

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for starting the game
@app.route('/start_game', methods=['POST'])
def start_game():
    start_game_logic()  # Call your game logic to set up the game
    return redirect(url_for('game'))

# Route for displaying the game page
@app.route('/game')
def game():
    # Render the game with necessary info (you can show current game state here)
    return render_template('game.html', characters=characters, powers=powers, health=health, inventory=inventory)

# Route for the fight page
@app.route('/fight', methods=['POST'])
def fight_route():
    result = fight()  # This would run the fight logic from game.py
    return render_template('result.html', result=result)  # Show the result of the fight

if __name__ == "__main__":
    app.run(debug=True)
