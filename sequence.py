# sequence.py
# represents a horizontal, vertical, or diagonal group of four connected spaces
# J. Hassler Thurston
# Connect Four
# December 31, 2013

class Sequence:
	def __init__(self, playing_board, startsquare, direction):
		self.playing_board = playing_board
		# startsquare is a 2-tuple representing the column/row of the starting square of the sequence
		self.startsquare = startsquare
		# direction is an integer (between 0 and 3) representing the direction of the sequence
		self.direction = direction
		# boolean representing whether this sequence is well-defined
		self.isValid = self.validate()
		if self.isValid:
			# direction_tuple is a 2-tuple representing the change in direction that the direction parameter encompasses
			self.direction_tuple = self.direction_to_tuple()
			# squares_in_sequence is a list of tuples representing which squares are in the sequence
			self.squares_in_sequence = [(startsquare[0] + self.direction_tuple[0]*i, startsquare[1] + self.direction_tuple[1]*i) 
				for i in range(4)]
			# This function updates the chips in the sequence and the categories for this sequence
			# Should be called whenever a new chip is placed into the sequence
			self.update()

	# makes sure this sequence is a valid sequence
	def validate(self):
		# validate the direction parameter
		if self.direction < 0 or self.direction > 3:
			print str(self.direction) + " is not a valid direction."
			return False
		# validate the column parameter
		elif self.startsquare[0] < 0 or self.startsquare[0] >= self.playing_board.columns:
			print "The column in " + str(self.startsquare) + " is not a valid column."
			return False
		# validate the row parameter
		elif self.startsquare[1] < 0 or self.startsquare[1] >= self.playing_board.rows:
			print "The row in " + str(self.startsquare) + " is not a valid column."
			return False
		# validate the squares in the sequence
		else:
			if (direction == 0 or direction == 2) and self.startsquare[1]+3 >= self.playing_board.rows:
				print "Some squares in this sequence are not on the board."
				return False
			elif (direction == 1 or direction == 2 or direction == 3) and self.startsquare[0]+3 >= self.playing_board.columns:
				print "Some squares in this sequence are not on the board."
				return False
			elif direction == 3 and self.startsquare[1]-3 < 0:
				print "Some squares in this sequence are not on the board."
				return False
			else: return True


	def direction_to_tuple(self):
		# 0 represents vertical
		if self.direction == 0:
			return (0,1)
		# 1 represents horizontal
		elif self.direction == 1:
			return (1,0)
		# 2 represents upper-diagonal
		elif self.direction == 2:
			return (1,1)
		# 3 represents lower-diagonal
		elif self.direction == 3:
			return (1,-1)
		# any other number isn't a valid direction (we should have already checked for direction validity)
		else:
			return (0,0)

	# updates the state of the sequence
	def update(self):
		# update the chips in the sequence
		self.chips_in_sequence = [playing_board.board[self.squares_in_sequence[i][0]][self.squares_in_sequence[i][1]]
			for in in range(4)]
		# update the properties of this sequence, depending on the chips in the sequence
		# sets self.chip_count to a 2-tuple representing the number of chips in the sequence for each player
		self.count_chips()
		# returns a string representing the basic state of the sequence
		self.get_basic_category()
		# returns a string representing the forced state of the sequence
		self.get_force_category()

	# updates the chip count in the sequence
	def count_chips(self):
		# from http://stackoverflow.com/questions/15375093/python-get-number-of-items-from-listsequence-with-certain-condition
		player1_chips = sum(1 for i in range(4) if self.chips_in_sequence[i] == 1)
		player2_chips = sum(1 for i in range(4) if self.chips_in_sequence[i] == 2)
		self.chip_count = (player1_chips, player2_chips)

	# updates the basic state of the sequence
	# should be called after self.count_chips() is called
	def get_basic_category(self):
		if self.chip_count == (0,0):
			# no chips of either player are in the sequence
			return "Unclaimed"
		elif self.chip_count[0] == 4:
			# Player 1 has gotten 4-in-a-row
			return "Won" # winning/losing are defined in terms of Player 1
		elif self.chip_count[1] == 4:
			# Player 2 has gotten 4-in-a-row
			return "Lost"
		elif self.chip_count[0] != 0 and self.chip_count[1] != 0:
			# each player has at least one chip in the sequence; the sequence can never be won
			return "Dead"
		# If we get to this point, we know that one player doesn't have any chips in the sequence
		elif self.chip_count[1] == 0:
			# Player 1 has made a claim to the sequence
			return "Claimed 1"
		elif self.chip_count[0] == 0:
			# Player 2 has made a claim to the sequence
			return "Claimed 2"
		else:
			# return an error
			print "Impossible to determine a basic category for this sequence."
			return ""

	# updates the forced state of the sequence
	def get_force_category(self):
		pass # update later








