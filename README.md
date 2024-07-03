# The Hidden Treasure

A simple Python game using the Turtle graphics library where the player navigates through a maze to collect eggs and avoid enemies.

## Game Overview

The objective of the game is to collect all the eggs (`E`) while avoiding the enemies (`A`). The player (`P`) moves through the maze using the arrow keys.

## Game Controls

- **Arrow Keys**: Move the player up, down, left, or right.

## Game Characters

- **Player (P)**: Represented by a green turtle. The player can move up, down, left, or right.
- **Egg (E)**: Represented by a gold circle. Collecting an egg increases the player's score by 100 points.
- **Enemy (A)**: Represented by a red triangle. The enemy moves randomly and follows the player when close.

## Game Map

- **X**: Wall block. The player and enemies cannot move through these blocks.

## Screenshots

### Game Start
<img src="https://github.com/chamindu2001/Hidden-Treasure-Game/assets/127916715/de281071-f582-4e12-8f9d-90e52e2c1006" width="400">

### Game Play
<img src="https://github.com/chamindu2001/Hidden-Treasure-Game/assets/127916715/49a55c01-11a8-4220-95b3-744f51f85a01" width="400">

### Game Over
<img src="https://github.com/chamindu2001/Hidden-Treasure-Game/assets/127916715/7acc69a0-dd1b-43fa-bce3-0c958fbdbba5" width="400">

## Getting Started

### Prerequisites

- Python 3.x
- Turtle graphics library (usually included with Python)

### Running the Game

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/the-hidden-treasure.git
    ```
2. Navigate to the project directory:
    ```bash
    cd the-hidden-treasure
    ```
3. Run the game:
    ```bash
    python game.py
    ```

## Code Explanation

### Block Class

Creates and manages the wall blocks in the game.

### Player Class

Manages the player's movement and collision detection with other game objects.

### Egg Class

Manages the eggs in the game, including their position and removal after collection.

### Enemy Class

Manages the enemies, including their random movement and chasing behavior.

### Setup Function

Sets up the game level by creating wall blocks, placing the player, eggs, and enemies.

### Main Game Loop

Runs the game, checking for collisions between the player and eggs or enemies, updating the score, and displaying messages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Python community for the amazing resources and tutorials.

