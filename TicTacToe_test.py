from TicTacToe import TicTacToe
from TicTacToe import STATES

def test_cross_win():
	game = TicTacToe()
	game.place_marker(0,0)
	game.place_marker(0,1)
	game.place_marker(1,1)
	game.place_marker(0,2)
	game.place_marker(2,2)
	assert game.state == STATES.CROSS_WON

def test_naught_win():
	game = TicTacToe()
	game.place_marker(0,0)
	game.place_marker(0,2)
	game.place_marker(0,1)
	game.place_marker(1,1)
	game.place_marker(1,0)
	game.place_marker(2,0)
	assert game.state == STATES.NAUGHT_WON

def test_draw():
	game = TicTacToe()
	game.place_marker(0,0)
	game.place_marker(0,1)
	game.place_marker(0,2)
	game.place_marker(1,0)
	game.place_marker(1,2)
	game.place_marker(1,1)
	game.place_marker(2,0)
	game.place_marker(2,2)
	game.place_marker(2,1)
	assert game.state == STATES.DRAW

def test_restart():
	game = TicTacToe()
	game.place_marker(0,0)
	game.place_marker(0,2)
	game.place_marker(0,1)
	game.place_marker(1,1)
	game.place_marker(1,0)
	game.place_marker(2,0)
	game.restart()
	assert game.board == [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
