# Rock Paper Scissors Game - Student Instructions

## Overview

You've been provided with two files:
1. The Rock Paper Scissors game executable (`game`)
2. A bot file (`your_bot.py`) that you can modify to implement your own strategy

## How to Play

1. Make sure both files are in the same directory
2. Modify `your_bot.py` to implement your strategy (instructions below)
3. Run the game executable:
   - On macOS/Linux: write `./rps_game` in terminal

## Creating Your Bot

Open `your_bot.py` in a text editor (VS Code, etc.) and modify the `get_move()` method.

Your bot must return one of three moves:
- `self.ROCK`
- `self.PAPER`
- `self.SCISSORS`

You can also change the `BOT_MODE` to either "normal" or "hard" to adjust the difficulty.

### Strategy Ideas

Consider implementing these strategies:
- Use randomness
- Analyze patterns in the game
- Implement counters to common strategies
- Use game theory principles

### Example Strategy

```python
def get_move(self):
    self.round_number += 1
    
    # Random strategy
    import random
    moves = [self.ROCK, self.PAPER, self.SCISSORS]
    move = random.choice(moves)
    
    # Record move for future reference
    self.my_previous_moves.append(move)
    return move
```

## Testing

As you modify your bot, simply save the file and run the game again. The game will load the latest version of your bot each time it runs.

## Rules

- First to win 3 rounds wins the game
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

Good luck! 
