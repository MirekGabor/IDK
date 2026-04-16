from flask import Flask, render_template, request, jsonify, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    # Initialize game in session
    if 'secret_number' not in session:
        session['secret_number'] = random.randint(1, 50)
        session['guesses_left'] = 5
        session['game_over'] = False
    return render_template('index.html')

@app.route('/api/guess', methods=['POST'])
def make_guess():
    data = request.json
    guess = data.get('guess')

    if session.get('game_over'):
        return jsonify({'error': 'Game is over. Please reset.'}), 400

    try:
        guess = int(guess)
        if guess < 1 or guess > 50:
            return jsonify({'error': 'Please enter a number between 1 and 50!'}), 400

        secret = session['secret_number']
        session['guesses_left'] -= 1

        result = {
            'guesses_left': session['guesses_left'],
            'game_over': False,
            'won': False,
            'lost': False,
            'feedback': ''
        }

        if guess == secret:
            result['won'] = True
            result['game_over'] = True
            result['feedback'] = '🎮 YOU WIN! Minecraft mode activated! 🎮'
            session['game_over'] = True
        elif guess < secret:
            result['feedback'] = 'Too low! Try again.'
        else:
            result['feedback'] = 'Too high! Try again.'

        if session['guesses_left'] == 0 and guess != secret:
            result['lost'] = True
            result['game_over'] = True
            result['feedback'] = f'😭 GAME OVER! 😭\nThe number was {secret}'
            session['game_over'] = True

        return jsonify(result)

    except ValueError:
        return jsonify({'error': 'Please enter a valid number!'}), 400

@app.route('/api/reset', methods=['POST'])
def reset_game():
    session['secret_number'] = random.randint(1, 50)
    session['guesses_left'] = 5
    session['game_over'] = False
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
