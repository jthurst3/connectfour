# compute_moves.py
# computes the best moves for a given state of a connect four game
# J. Hassler Thurston
# Connect Four
# December 31, 2013

# build up to this function
def compute_move(playing_board):
	# basic algorithm for computing a move:
	# identify the available squares where we can play
	squares 
	# check if we can play in a winning square
	# check if we can stop opponent from playing in a winning square
	# identify any combination of sequences, if they exist, where one of them can be won
	# identify such combinations of sequences for the opponent
	# play the move that maximizes the state function for you
	pass

# identifies a column for which we can play to win in 1 move, or -1 if none exists
def winning_square(playing_board):
	pass

# calculates the available spaces for a player to play
def availableMoves(playing_board):
	return [i for i in range(playing_board.columns) if playing_board.positions[i] < playing_board.rows]

