# Goblin Invasion

A simple arcade game written in Python using Pygame. The player controls an elven archer, repels waves of goblins, and defends the forest from being overrun.

## Project Inspiration

Based on a project by Eric Matthes from Python Crashcourse book.

## Requirements

- Python 3.10+ (recommended)
- Pygame 2.x

## Installation

1. Go to the project directory.
2. (Optional) Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install pygame
```

## Run

```bash
python goblin_invasion.py
```

## Controls

- Arrow keys: move the elf (left/right/up/down)
- Space: fire an arrow
- Q: quit the game
- Mouse: click the Play button on the start screen

## Game Rules

- Goblins move as a group, reverse direction at screen edges, and move downward.
- Hitting a goblin with an arrow removes it.
- After clearing a full wave, a new army is spawned.
- The player has a limited number of lives (default: 3).
- You lose a life when a goblin collides with the elf.
- You lose a life when a goblin reaches the bottom of the screen (the forest is breached).
- The game stops after all lives are lost.

## Project Structure

- goblin_invasion.py - main game loop and event logic
- settings.py - gameplay settings (speed, limits, army parameters)
- game_stats.py - game state and remaining lives
- elf.py - player class (movement, hit/loss visual states)
- goblin.py - enemy class and army movement
- arrow.py - projectile class
- button.py - game start button
- images/ - graphical assets
- ideas.txt - list of ideas and future improvements

## Further Development

Ideas currently noted in the project:

- add other goblins (red and blue),
- animate the elf's leg movement,
- add sound effects.
