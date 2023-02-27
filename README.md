# Ping Pong Game

This is a simple Ping Pong game implemented using Python's turtle module. The game is played by two players, each controlling a paddle that can move up and down to hit a ball back and forth. The game continues until one player misses the ball, and the opponent scores a point. The game ends when one player reaches a pre-determined score.

## Getting Started
To play the game, you need to have Python installed on your machine. You can download Python from the official website python.org.
Once you have python installed, follow these steps:

1. Clone this repository to your local machine
2. You also need to install the turtle module, which is included in the standard library of Python. To install it, open your terminal or command prompt and run the following command:
```
pip install turtle
```

## Usage
Clone this repository to your local machine using the following command:
```
python main.py
```
This will open a window with the game screen. 
The left player uses the "w" and "s" keys to move their paddle up and down, while the right player uses the up and down arrow keys. 
The objective of the game is to prevent the ball from hitting your side of the screen while trying to hit it towards your opponent's side.

## Files
The game consists of four Python files:
```
main.py - This file contains the main game loop and sets up the game screen and objects.
ball.py - This file contains the Ball class, which represents the ball object in the game.
paddle.py - This file contains the Paddle class, which represents the paddles used by the players.
scoreboard.py - This file contains the Scoreboard class, which keeps track of the players' scores.
```
