# compute_moves.py
# computes the best moves for a given state of a connect four game
# J. Hassler Thurston
# Connect Four
# December 31, 2013

import copy

# build up to this function
def compute_move(playing_board):
	# basic algorithm for computing a move:
	# initialize the resulting column to -1
	move = -1
	# check if we can play in a winning square
	move = winning_square(playing_board)
	if move != -1:
		playing_board.move(move)
		return True
	# check if we can stop opponent from playing in a winning square
	move = losing_square(playing_board)
	if move != -1:
		playing_board.move(move)
		return True
	# identify any combination of sequences, if they exist, where one of them can be won
	compute_combinations(playing_board, playing_board.turn)
	# identify such combinations of sequences for the opponent
	compute_combinations(playing_board, playing_board.opponent)
	# check if we can play a move that's part of a winning combination
	move = play_combination(playing_board)
	if move != -1:
		playing_board.move(move)
		return True
	# otherwise, play the move that maximizes the state function for you
	playing_board.move(maximize_state_function(playing_board))
	return True

# identifies a column for which we can play to win in 1 move, or -1 if none exists
def winning_square(playing_board):
	for move in playing_board.available_squares:
		# if making this move will instantly win,
		if move in playing_board.winning_squares[playing_board.turn-1]:
			# return the relevant column
			return move[0]
	# otherwise, return -1
	return -1

# identifies a column for which we can play to not lose in 1 move, or -1 if none exists
def losing_square(playing_board):
	for move in playing_board.available_squares:
		# if making this move will instantly make us not lose,
		if move in playing_board.winning_squares[playing_board.opponent-1]:
			# return the relevant column
			return move[0]
	# otherwise, return -1
	return -1

# calculates the available spaces for a player to play
def availableMoves(playing_board):
	return [(i, playing_board.positions[i]) for i in range(playing_board.columns) if playing_board.positions[i] < playing_board.rows]

# checks to see if there are any winning combinations for a given player
# for each pair of a player's claimed sequences, check if we can play a move that would win one of those sequences
def compute_combinations(playing_board, player):
	# get claimed sequences for the given player
	claimed_sequences = find_sequences(playing_board, "Claimed " + str(player))
	# compute pairs of these sequences
	sequence_pairs = [(claimed_sequences[i], claimed_sequences[j]) for i in range(len(claimed_sequences))
		for j in range(len(claimed_sequences)) if i < j]
	# see how this pair can be made into a winning pair
	# LEFT OFF HERE

# returns all sequences on the board in the specified category
def find_sequences(playing_board, category):
	sequence_list = []
	for i in range(playing_board.columns):
		for j in range(playing_board.rows):
			for sequence in playing_board.sequences[i][j]:
				if sequence.category == category:
					sequence_list.append(sequence)
	return sequence_list

# identifies a move that will lead to a win (if one exists)
def play_combination(playing_board):
	# default
	return -1

# calculates the state function for the board
def state_function(playing_board):
	# The state function is an incomplete representation of which player is winning,
	# based on the number of sequences in the given categories.
	# It is an integer between [] and [], with a positive integer representing an advantage for Player 1,
	# a negative integer representing an advantage for Player 2,
	# and 0 representing equality.
	# Each unclaimed sequence or dead sequence is worth 0,
	# a sequence that's won or will be won with perfect play makes the state function True
	# a sequence that's lost or will be lost even with perfect play makes the state function False
	# Each sequence that's claimed by player 1 will add the number of chips in the sequence to the state function
	# Each sequence that's claimed by player 2 will subtract the number of chips in the sequence to the state function
	##########
	# initialize the function's value to 0
	value = 0
	# enumerate the sequences
	for i in range(playing_board.columns):
		for j in range(playing_board.rows):
			for sequence in playing_board.sequences[i][j]:
				# get the value of the sequence
				sequence_value = sequence.get_value()
				# if the sequence has been Won or Lost, make the value a boolean
				if sequence_value == 4:
					return True
				elif sequence_value == -4:
					return False
				else:
					# add the value of the sequence to the state function
					value += sequence.get_value()
	# return the value
	return value

# computes the move that maximizes the state function for the player whose turn it is
def maximize_state_function(playing_board):
	# make an array of playing boards for each column (we need to use copy.deepcopy())
	next_move_array = [copy.deepcopy(playing_board) for i in range(len(playing_board.available_columns))]
	# pretend to make moves on each of these boards
	moves = [next_move_array[i].move(playing_board.available_columns[i]) for i in range(len(playing_board.available_columns))]
	# compute state functions
	state_functions_array = [state_function(next_move_array[i]) for i in range(len(playing_board.available_columns))]
	# pick the index that maximizes/minimizes the state function
	# from http://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
	if playing_board.turn == 1:
		best_index = state_functions_array.index(max(state_functions_array))
	else:
		best_index = state_functions_array.index(min(state_functions_array))
	# compute the relevant column from the index
	return playing_board.available_columns[best_index]





