# 2048 Python Game

A Python implementation of the popular 2048 game. This version includes a scoring system, a high score feature, customizable grid size, and the ability to stop the game while saving your score. Additionally, if the player reaches the 2048 tile, they are given the option to continue playing or stop.

## Features

- **Dynamic Grid Size**: Choose the size of the grid before starting the game.
- **Score Tracking**: The game tracks your score and compares it to your highest score.
- **High Score Persistence**: The high score is saved in a file (`high_score.txt`) and persists between game sessions.
- **2048 Tile Win Condition**: When the player reaches the 2048 tile, they are notified of their win and can choose to continue playing or stop the game.
- **Stop Game Anytime**: The player can type `stop` to quit the game, which will save the current score.

## How to Play

- **Controls**:
  - `z` - Move Up
  - `q` - Move Left
  - `s` - Move Down
  - `d` - Move Right
  - `stop` - Stop the game and save your score

- **Objective**: Combine tiles with the same number to create a tile with the value 2048. Once you reach 2048, you can choose to continue playing or stop.

## Installation

1. Ensure you have Python 3 installed.
2. Clone this repository or download the `2048.py` file.

    ```bash
    git clone https://github.com/RaphRoss/2048.git
    cd 2048
    ```

3. Install the required dependencies. The game uses NumPy, so you need to install it if you don't already have it:

    ```bash
    pip install numpy
    ```

## Running the Game

Run the game using Python:

```bash
python 2048.py
