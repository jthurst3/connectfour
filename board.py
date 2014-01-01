# board.py
# initializes the Connect Four board
# J. Hassler Thurston
# Connect Four
# December 30, 2013

# from win import *
from pattern import *
from sequence import *
from compute_moves import *

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
		self.opponent = 2
		# nobody has won yet
		self.winner = 0
		# nobody has even moved yet
		self.last_move = -1
		# the positions array will keep track of the legal places to place the next chip
		self.positions = [0 for i in range(columns)]
		# a 2D array of all the well-defined sequences on the board
		self.initSequences()
		# an array representing the available squares for a player
		self.available_squares = availableMoves(self)
		# a similar array representing the available columns for a player
		self.available_columns = [square[0] for square in self.available_squares]
		# a 2D array representing the squares that a player can play in to win the game
		self.winning_squares = [[], []]

	# initializes all well-defined sequences for the board
	def initSequences(self):
		# set the global variable
		self.sequences = [[[] for j in range(self.rows)] for i in range(self.columns)]
		# vertical sequences
		for i in range(self.columns):
			for j in range(self.rows - 3):
				self.sequences[i][j].append(Sequence(self, (i,j), 0))
		# horizontal sequences
		for i in range(self.columns - 3):
			for j in range(self.rows):
				self.sequences[i][j].append(Sequence(self, (i,j), 1))
		# upper-diagonal sequences
		for i in range(self.columns - 3):
			for j in range(self.rows - 3):
				self.sequences[i][j].append(Sequence(self, (i,j), 2))
		# lower-diagonal sequences
		for i in range(self.columns - 3):
			for j in range(3, self.rows):
				self.sequences[i][j].append(Sequence(self, (i,j), 3))

	# tries to put a piece into the relevant column on the board.
	# returns a boolean: True if the piece is successfully placed on the board,
	# False otherwise.
	def move(self, column):
		# check to see if someone has already won
		if self.winner != 0:
			print "Player " + str(self.winner) + " has already won."
			return False
		# columns and rows are numbered starting at 0.
		# check if we entered a well-defined column
		if(column < 0 or column >= self.columns):
			print("Column " + str(column) + " doesn't exist.")
			return False
		# check to see if that column is filled up
		if(self.positions[column] == self.rows):
			print("Column " + str(column) + " is filled up.")
			return False
		# If all is well, put the player's piece onto the board,
		self.board[column][self.positions[column]] = self.turn
		# set the last move to the current move
		self.last_move = column
		# change turns,
		self.turn = (self.turn % 2) + 1
		self.opponent = (self.opponent % 2) + 1
		# update the positions array,
		self.positions[column] += 1
		# update the relevant sequences,
		self.update_sequences(column)
		# update the available squares,
		self.available_squares = availableMoves(self)
		# update the available columns,
		self.available_columns = [square[0] for square in self.available_squares]
		# update the winning squares,
		self.update_winning_squares()
		# update the winner if someone has won,
		if self.is_game_over():
			self.winner = self.turn
			print "Player " + str(self.winner) + " has just won!"
			return True
		# and return True
		return True

	# attempts to make a sequence of moves
	# returns a boolean: True if all the moves are legal, False otherwise.
	def move_sequence(self, column_array):
		moves = map(self.move, column_array)
		return all(moves)

	# returns a list of sequences that have the given square in them
	def find_sequences(self, square):
		sequence_list = []
		sequence_list.extend(self.find_vertical_sequences(square))
		sequence_list.extend(self.find_horizontal_sequences(square))
		sequence_list.extend(self.find_upper_diagonal_sequences(square))
		sequence_list.extend(self.find_lower_diagonal_sequences(square))
		return sequence_list
	# finds all vertical sequences that contain the given square
	def find_vertical_sequences(self, square):
		# tuple representing the vertical direction
		d_tuple = direction_tuple(0)
		# number of sequences
		num_sequences = min(4,square[1]+1)
		# list of all possible sequences (some will be False)
		sequences = [self.find_sequence(square, 0, i) for i in range(num_sequences)]
		# from http://stackoverflow.com/questions/1157106/remove-all-occurences-of-a-value-from-a-python-list
		return filter(lambda a: a != False, sequences)
	# finds all horizontal sequences that contain the given square
	def find_horizontal_sequences(self, square):
		# tuple representing the horizontal direction
		d_tuple = direction_tuple(1)
		# number of sequences
		num_sequences = min(4,square[0]+1)
		# list of all possible sequences (some will be False)
		sequences = [self.find_sequence(square, 1, i) for i in range(num_sequences)]
		# from http://stackoverflow.com/questions/1157106/remove-all-occurences-of-a-value-from-a-python-list
		return filter(lambda a: a != False, sequences)
	# finds all upper_diagonal sequences that contain the given square
	def find_upper_diagonal_sequences(self, square):
		# tuple representing the upper_diagonal direction
		d_tuple = direction_tuple(2)
		# number of sequences
		num_sequences = min(4,square[1]+1,square[0]+1)
		# list of all possible sequences (some will be False)
		sequences = [self.find_sequence(square, 2, i) for i in range(num_sequences)]
		# from http://stackoverflow.com/questions/1157106/remove-all-occurences-of-a-value-from-a-python-list
		return filter(lambda a: a != False, sequences)
	# finds all lower_diagonal sequences that contain the given square
	def find_lower_diagonal_sequences(self, square):
		# tuple representing the lower_diagonal direction
		d_tuple = direction_tuple(3)
		# number of sequences
		num_sequences = min(4,square[0]+1,self.rows-square[1])
		# list of all possible sequences (some will be False)
		sequences = [self.find_sequence(square, 3, i) for i in range(num_sequences)]
		# from http://stackoverflow.com/questions/1157106/remove-all-occurences-of-a-value-from-a-python-list
		return filter(lambda a: a != False, sequences)

	# returns the sequence that overlaps with a given square, satisfying the extra criteria
	# If no such sequence exists, this method returns False
	def find_sequence(self, square, direction, square_number):
		# make sure the square number is valid
		if square_number < 0 or square_number > 3:
			print "Square number " + str(square_number) + " doesn't exist."
			return False
		# make sure the direction is valid
		if direction < 0 or direction > 3:
			print "Direction " + str(direction) + " doesn't exist."
			return False
		# make sure the square is valid
		if square[0] < 0 or square[0] >= self.columns or square[1] < 0 or square[1] >= self.rows:
			print "Square " + str(square) + " doesn't exist."
			return False
		# make sure there would be four squares in such a sequence
		# get the direction tuple
		d_tuple = direction_tuple(direction)
		# get the starting square
		starting_square = (square[0] - square_number*d_tuple[0],
			square[1] - square_number*d_tuple[1])
		# get the ending square
		ending_square = (square[0] - (square_number-3)*d_tuple[0],
			square[1] - (square_number-3)*d_tuple[1])
		if starting_square[0] < 0 or starting_square[0] >= self.columns or starting_square[1] < 0 or starting_square[1] >= self.rows:
			# print "Sequence doesn't exist."
			return False
		if ending_square[0] < 0 or ending_square[0] >= self.columns or ending_square[1] < 0 or ending_square[1] >= self.rows:
			# print "Sequence doesn't exist."
			return False
		# if everything is valid, try to find such a sequence:
		# search for the relevant list of sequences in self.sequences
		for sequence in self.sequences[starting_square[0]][starting_square[1]]:
			# limit these sequences to ones in which the direction matches
			if sequence.direction == direction:
				# limit the remaining sequences to those where the given square appears at position square_number in the sequence
				if sequence.squares_in_sequence[square_number] == square:
					# note: there can only be one sequence with these criteria
					return sequence
		# if no such sequence is found, return False
		return False

	# updates the relevant sequences after a move
	# should be called after positions array is updated
	def update_sequences(self, column):
		row = self.positions[column] - 1
		# list of all sequences that overlap with the relevant square
		sequence_list = self.find_sequences((column, row))
		# update each sequence
		for sequence in sequence_list:
			sequence.update()
			# eliminate the dead sequences
			if sequence.category == "Dead":
				self.eliminate_sequence(sequence)

	# recomputes the winning squares after a move
	# should be called after positions array is updated
	def update_winning_squares(self):
		# clear the winning squares
		self.winning_squares = [[], []]
		# iterate over all sequences
		for i in range(self.columns):
			for j in range(self.rows):
				for sequence in self.sequences[i][j]:
					# for each sequence, add a winning square if one exists and is unique
					if sequence.winning_square != (-1,-1):
						player = sequence.owner
						if sequence.winning_square not in self.winning_squares[player-1]:
							self.winning_squares[player-1].append(sequence.winning_square)

	# remove the given sequence from the list of sequences
	def eliminate_sequence(self, sequence):
		# find the sequence's starting square
		starting_square = sequence.startsquare
		# remove it from the list
		self.sequences[starting_square[0]][starting_square[1]].remove(sequence)

	# check if a player has won
	def is_game_over(self):
		# enumerate the sequences
		for i in range(self.columns):
			for j in range(self.rows):
				for sequence in self.sequences[i][j]:
					if sequence.category == "Won" or sequence.category == "Lost":
						return True
		return False

	###### STATISTICS
	# count the total number of sequences on the board
	def num_sequences(self):
		total = 0
		for i in range(self.columns):
			for j in range(self.rows):
				total += len(self.sequences[i][j])
		return total
	# count the number of sequences in each starting position
	def enumerate_sequences(self):
		return [[len(self.sequences[i][j]) for j in range(self.rows)] for i in range(self.columns)]












