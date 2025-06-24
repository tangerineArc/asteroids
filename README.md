# Asteroids

Asteroids is a classic arcade-style game where you pilot a spaceship and try not to get obliterated by floating space rocks.
The game includes real-time movement, asteroid generation, collision detection, and a game loop that just won’t quit until you do.

## What it Offers?

- Player-controlled spaceship with smooth rotation _(thrust-based movement coming soon)_
- Randomly spawning asteroids that float in space and try to ruin your ship
- Simple collision logic for destroying your ship


## Tech Stack

- **Python** - the programming language for non-programmers
- **Pygame** - 2D game development library for Python

## Repo Structure

- `asteroid.py` - class definition and render logic for asteroids
- `asteroidfield.py` - collision-detection and spawn logic
- `circleshape.py` - abstract class for circle shape
- `constants.py` - global constants for game environment
- `main.py` - main driver code with game loop
- `player.py` - class definition and logic for spaceship
- `shot.py` - class definition for spaceship bullets

## Setup and Usage

### Prerequisites

- Python 3.10+ installed
- Access to a unix-like shell (e.g. zsh or bash)

### Steps

1. Navigate to the project directory and create a virtual environment at the top level:

    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```
    You should now see `(venv)` at the beginning of your terminal prompt.

3. Install the requirements:

    ```bash
    pip3 install -r requirements.txt
    ```

4. Run the game with:

    ```bash
    python3 main.py
    ```

5. Enjoy :)

## Snapshot

> _I am not good at this_ :(

[![output4.gif](https://i.postimg.cc/RCgpNpr9/output4.gif)](https://postimg.cc/qgCxFLMZ)
