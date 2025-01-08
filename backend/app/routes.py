from flask import Flask, request, jsonify
from game import send_move_to_stockfish, get_stockfish_evaluation, get_stockfish_best_move

app = Flask(__name__)

@app.route('/move', methods=['POST'])
def send_move():
    """
    Endpoint to send moves to Stockfish.
    Expects a JSON payload with "moves" field containing chess moves.
    """
    data = request.json
    moves = data.get("moves")
    if not moves:
        return jsonify({"error": "No moves provided"}), 400
    try:
        send_move_to_stockfish(moves)
        return jsonify({"message": "Move sent successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/evaluation', methods=['GET'])
def get_evaluation():
    """
    Endpoint to get the evaluation of the current position.
    """
    try:
        evaluation = get_stockfish_evaluation()
        return jsonify(evaluation)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/best-move', methods=['GET'])
def get_best_move():
    """
    Endpoint to get the best move for the current position.
    """
    try:
        best_move = get_stockfish_best_move()
        return jsonify({"best_move": best_move})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)