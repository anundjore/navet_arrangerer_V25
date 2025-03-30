# Choose which bot you will play against: "normal" or "hard"
BOT_MODE = "normal"  # Change to "hard" to play against a more difficult bot, warning: it's hard


class YourBot:
    # Constants for moves
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    def __init__(self):
        self.previous_opponent_move = None 

    def get_move(self, opponent_move=None):
        if opponent_move: 
            self.previous_opponent_move = opponent_move




        # Code to be modified by you is found under here.
        # previous_opponent_move is the last used move by the opponent
        # Here you can try different strategies
        # you return a move for each turn, which gets returned at the end of the method

        # MODIFY THIS CODE

        if self.previous_opponent_move == self.SCISSORS:
            move = self.SCISSORS
        elif self.previous_opponent_move == self.ROCK:
            move = self.SCISSORS
        else:
            move = self.SCISSORS

        # MODIFY THIS CODE

        # dont change this line
        return move

