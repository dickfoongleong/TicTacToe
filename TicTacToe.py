from enum import Enum

class STATES(Enum):
	"""Tic-Tac-Tow states"""
	CROSS_TURN = 0
	NAUGHT_TURN = 1
	DRAW = 2
	CROSS_WON = 3
	NAUGHT_WON = 4

class TicTacToe:
	"""Tic-Tac-Tow game instance."""
	def __init__(self):
		self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
		self.state = STATES.CROSS_TURN

	def place_marker(self, row, column):
		"""Place a marker on to the position of the board based on current game turns. This method updates the game state after every move."""
		if self.board[row][column] == ' ':
			if self.state == STATES.CROSS_TURN:
				self.board[row][column] = 'X'
				if self.is_winner('X'):
					self.state = STATES.CROSS_WON
				else:
					self.state = STATES.NAUGHT_TURN
			elif self.state == STATES.NAUGHT_TURN:
				self.board[row][column] = 'O'
				if self.is_winner('O'):
					self.state = STATES.NAUGHT_WON
				else:
					self.state = STATES.CROSS_TURN
			if self.is_draw():
				self.state = STATES.DRAW
			self.display()
		elif self.is_draw():
			self.state = STATES.DRAW

	def is_winner(self, symbol):
		"""Check if the current symbol won."""
		for i in range(3):
			row = self.board[i]
			if row[0] == symbol and row[1] == symbol and row[2] == symbol:
				return True

		for i in range(3):
			if self.board[0][i] == symbol and self.board[1][i] == symbol and self.board[2][i] == symbol:
				return True

		if self.board[0][0] == symbol and self.board[1][1] == symbol and self.board[2][2] == symbol:
			return True

		if self.board[0][2] == symbol and self.board[1][1] == symbol and self.board[2][0] == symbol:
			return True
		return False

	def is_draw(self):
		"""Check if the current game is draw."""
		for row in self.board:
			if ' ' in row:
				return False
		return True

	def restart(self):
		"""Restart the game by setting the board back to empty and state to CROSS_TURN."""
		self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
		self.state = STATES.CROSS_TURN

	def display(self):
		"""Print the board of the game."""
		print('\n'.join([' | '.join([c for c in row]) for row in self.board]),end='\n\n')
