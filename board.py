# board.py
# initializes the Connect Four board
# J. Hassler Thurston
# Connect Four
# December 30, 2013

# from win import *
from pattern import *
from sequence import *

class Board:
	def __init__(self, columns, rows):
		if(columns < 4 or rows < 4):
			print("Too few rows or columns.")
			return;
		self.rows = rows
		self.columns = columns
		# The Connect Four board will be represented by a 2D array, where the length of the big array
		# is the number of columns, each little array represents a column, and the length of a sub-array
		# is equal to the number of rows.
		# Initially, the board will be filled up with 0s, to signify that no chips have been played.
		self.board = [[0 for j in range(rows)] for i in range(columns)]
		# The person playing first will be represented by a 1, and the second person by a 2.
		self.turn = 1
		# the positions array will keep track of the legal places to place the next chip
		self.positions = [0 for i in range(columns)]
		# a 2D array representing the squares that a player can play in to win the game
		self.winning_squares = [[], []]

	# tries to put a piece into the relevant column on the board.
	# returns a boolean: True if the piece is successfully placed on the board,
	# false otherwise.
	def move(self, column):
		# columns and rows are numbered starting at 0.
		# check if we entered a well-defined column
		if(column < 0 or column >= self.columns):
			print("Column " + str(column) + " doesn't exist.")
			return False
		# check to see if that column is filled up
		if(self.positions[column] == self.rows):
			print("Column " + str(column) + " is filled up.")
			return False
		# If all is well, put the player's piece onto the board, change turns, update the positions array, and return True
		self.board[column][self.positions[column]] = self.turn
		self.turn = (self.turn % 2) + 1
		self.positions[column] += 1
		print win(self, column), pattern(self, column, self.positions[column]-1, [(self.turn%2)+1 for i in range(4)])
		return True

	# calculates the available spaces for a player to play
	def availableMoves(self):
		return [i for i in range(self.columns) if self.positions[i] < self.rows]





