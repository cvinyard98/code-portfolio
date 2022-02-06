# Overview

Conway's Game of Life is a 1 player game without an objective.
In it, there is a grid of cells, each of which is either "dead" or "alive". 
The player sets the grid initially, setting some cells as alive while leaving the rest dead. 
Each turn, cells can come to life or die or stay in the state that they were in previously, according to the following rules:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

This version of the game advances one turn each time the spacebar is pressed. The board is cleared if the "C" key is pressed.

[Software Demo Video](https://youtu.be/4YZrjuFzteE)

# Development Environment

I made this project using Python. I used the Pyarcade library extensively.


# Useful Websites

{Make a list of websites that you found helpful in this project}
* [RealPython.com](https://realpython.com/arcade-python-game-framework/)
* [Arcade Academy](https://api.arcade.academy/en/latest/examples/index.html)

# Future Work


* Better interface including onscreen buttons, rules and instructions, and a menu
* Ability to advance the process continually
* Sound effects
