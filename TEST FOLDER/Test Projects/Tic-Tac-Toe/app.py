from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Game State
board = {f"{r}{c}": " " for r in ['a', 'b', 'c'] for c in ['1', '2', '3']}
current_player = "X"
winner = None
draw = False

def check_win(board, symbol):
    # Horizontal
    if board['a1'] == symbol and board['b1'] == symbol and board['c1'] == symbol: return True
    if board['a2'] == symbol and board['b2'] == symbol and board['c2'] == symbol: return True
    if board['a3'] == symbol and board['b3'] == symbol and board['c3'] == symbol: return True
    
    # Vertical
    if board['a1'] == symbol and board['a2'] == symbol and board['a3'] == symbol: return True
    if board['b1'] == symbol and board['b2'] == symbol and board['b3'] == symbol: return True
    if board['c1'] == symbol and board['c2'] == symbol and board['c3'] == symbol: return True
    
    # Diagonal
    if board['a1'] == symbol and board['b2'] == symbol and board['c3'] == symbol: return True
    if board['c1'] == symbol and board['b2'] == symbol and board['a3'] == symbol: return True
    
    return False

def check_draw(board):
    return all(value != " " for value in board.values())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/state')
def get_state():
    return jsonify({
        'board': board,
        'current_player': current_player,
        'winner': winner,
        'draw': draw
    })

@app.route('/move', methods=['POST'])
def move():
    global current_player, winner, draw
    
    if winner or draw:
        return jsonify({'status': 'game_over'})
        
    data = request.json
    cell = data.get('cell')
    
    if cell in board and board[cell] == " ":
        board[cell] = current_player
        
        if check_win(board, current_player):
            winner = current_player
        elif check_draw(board):
            draw = True
        else:
            current_player = "O" if current_player == "X" else "X"
            
        return jsonify({'status': 'success', 'board': board, 'current_player': current_player, 'winner': winner, 'draw': draw})
    
    return jsonify({'status': 'invalid'})

@app.route('/reset', methods=['POST'])
def reset():
    global board, current_player, winner, draw
    board = {f"{r}{c}": " " for r in ['a', 'b', 'c'] for c in ['1', '2', '3']}
    current_player = "X"
    winner = None
    draw = False
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(debug=True)
