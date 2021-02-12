from TicTacToe import TicTacToe
from TicTacToe import STATES
import random

game = TicTacToe()
while game.state == STATES.CROSS_TURN or game.state == STATES.NAUGHT_TURN:
	r = random.randint(0,2)
	c = random.randint(0,2)
	game.place_marker(r, c)
print("Game 1:", game.state.name, sep=' ')
