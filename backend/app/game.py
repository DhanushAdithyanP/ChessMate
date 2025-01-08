from stockfish_wrapper import StockfishWrapper

# Initialize the StockfishWrapper
stockfish_path = "/path/to/stockfish"  # Update with the actual path to Stockfish
stockfish = StockfishWrapper(stockfish_path)
stockfish.start_engine()

def send_move_to_stockfish(moves):
    """Send moves to Stockfish."""
    stockfish.send_move(moves)

def get_stockfish_evaluation():
    """Get evaluation from Stockfish."""
    return stockfish.get_evaluation()

def get_stockfish_best_move():
    """Get the best move from Stockfish."""
    return stockfish.get_best_move()