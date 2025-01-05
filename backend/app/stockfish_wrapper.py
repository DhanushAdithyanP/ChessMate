from stockfish import Stockfish

class StockfishWrapper:
    def __init__(self, stockfish_path="/Users/pdhanushadithyan/Desktop/Projects/ChessMate/stockfish/stockfish-macos-m1-apple-silicon"):
        """
        Initialize the Stockfish engine.

        Args:
            stockfish_path (str): Path to the Stockfish executable.
        """
        self.stockfish = Stockfish(path=stockfish_path)

    def start_engine(self):
        """Starts the Stockfish engine and sets default options."""
        self.stockfish.set_depth(15)
        self.stockfish.set_skill_level(20)

    def send_move(self, moves):
        """
        Sends moves to Stockfish.

        Args:
            moves (str): A string of moves (e.g., 'e2e4 e7e5').
        """
        self.stockfish.set_position(moves.split())

    def get_evaluation(self):
        """
        Gets the evaluation of the current position.

        Returns:
            dict: Evaluation details from Stockfish.
        """
        return self.stockfish.get_evaluation()

    def get_best_move(self):
        """
        Gets the best move from Stockfish.

        Returns:
            str: The best move (e.g., 'e2e4').
        """
        return self.stockfish.get_best_move()

    def reset_position(self):
        """Resets the board to the starting position."""
        self.stockfish.set_position([])

# Example usage
if __name__ == "__main__":
    stockfish_path = "/Users/pdhanushadithyan/Desktop/Projects/ChessMate/stockfish/stockfish-macos-m1-apple-silicon"  # Update with the actual path
    sf = StockfishWrapper(stockfish_path)
    
    sf.start_engine()
    sf.send_move("e2e4")
    print("Evaluation:", sf.get_evaluation())
    print("Best Move:", sf.get_best_move())
    