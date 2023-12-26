# Piskvorky Game

Piskvorky is a simple tic-tac-toe (piskvorky in Slovak) game developed using the Tkinter library in Python. It provides a graphical user interface for two players to take turns placing their symbols on a 3x3 grid. The game detects the winner when a player gets three of their symbols in a row horizontally, vertically, or diagonally. If no player achieves this, the game ends in a draw after all positions are filled.

## How to Play

1. Clone the Repository:
```git clone https://github.com/yourusername/piskvorky-game.git```

2. Navigate to the Project Directory:
```cd piskvorky-game```

3. Run the Game:
```python piskvorky.py```

4. Game Interface:
- The game window will open, displaying a 3x3 grid of buttons.
- Players take turns clicking on the buttons to place their symbols (X or O).
- The game will automatically detect a winner or a draw.

## Game Controls

- Each button represents a cell in the grid where players can place their symbols.
- Click on an empty button to place your symbol.
- If a player achieves three symbols in a row horizontally, vertically, or diagonally, they win.
- If all cells are filled and no player has won, the game ends in a draw.

## Components

1. Game Logic (piskvorky.py)

- Location: piskvorky.py

This script contains the main logic for the Piskvorky game, including handling player moves, checking for a winner, and updating the game state.

2. Tkinter GUI Setup

- Location: piskvorky.py

The Tkinter library is used to create the graphical user interface for the game. Buttons represent cells in the grid, and the game responds to player clicks.

License
This Piskvorky game is released under the MIT license. See the [LICENSE](LICENSE) file for details.
