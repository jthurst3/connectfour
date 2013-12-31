# pattern.py
# extension of the win functions
# J. Hassler Thurston
# Connect Four
# December 30, 2013

def pattern(playing_board, column, row, pattern):
	# We need to check for a pattern horizontally, vertically, and along the diagonals.
	horizontal = pattern_horizontal(playing_board, column, row, pattern)
	vertical = pattern_vertical(playing_board, column, row, pattern)
	up_diagonal = pattern_upDiagonal(playing_board, column, row, pattern)
	down_diagonal = pattern_downDiagonal(playing_board, column, row, pattern)
	return horizontal or vertical or up_diagonal or down_diagonal

def pattern_vertical(playing_board, column, row, pattern):
	if(playing_board.positions[column] < 4):
		return False
	relevant_chips = playing_board.board[column][-4:]
	return relevant_chips == pattern

def pattern_horizontal(playing_board, column, row, pattern):
	min_starting_column = max(0, column-3)
	max_starting_column = min(column, playing_board.columns-4)
	relevant_chips_array = [[playing_board.board[j][row] for j in range(i,i+4)] 
		for i in range(min_starting_column,max_starting_column+1)]
	return pattern in relevant_chips_array

def pattern_upDiagonal(playing_board, column, row, pattern):
	if(column < row):
		starting_spot = (0, row - column)
	else:
		starting_spot = (column - row, 0)
	num_elements = min(playing_board.columns-starting_spot[0], 
						playing_board.rows-starting_spot[1]) # the number of elements along the diagonal
	# if there aren't at least 4 elements on the diagonal, return false
	if(num_elements < 4):
		return False
	# otherwise:
	pos_starting_element = column - starting_spot[0] # the position of the last chip in the diagonal array
	starting_positions = range(max(pos_starting_element-3,0),min(num_elements-4,pos_starting_element)+1)
	relevant_diagonal = [playing_board.board[starting_spot[0]+i][starting_spot[1]+i] 
		for i in range(num_elements)] # the diagonal elements
	relevant_chips_array = [[relevant_diagonal[j] for j in range(i,i+4)] for i in starting_positions]
	return pattern in relevant_chips_array

def pattern_downDiagonal(playing_board, column, row, pattern):
	if(column < playing_board.rows-row):
		starting_spot = (0, row+column)
	else:
		starting_spot = (column-(playing_board.rows-1-row), playing_board.rows-1)
	num_elements = min(playing_board.columns-starting_spot[0], starting_spot[1]+1) # the number of elements along the diagonal
	# if there aren't at least 4 elements on the diagonal, return false
	if(num_elements < 4):
		return False
	# otherwise:
	pos_starting_element = column - starting_spot[0] # the position of the last chip in the diagonal array
	starting_positions = range(max(pos_starting_element-3,0),min(num_elements-4,pos_starting_element)+1)
	relevant_diagonal = [playing_board.board[starting_spot[0]+i][starting_spot[1]-i]
		for i in range(num_elements)] # the diagonal elements
	relevant_chips_array = [[relevant_diagonal[j] for j in range(i,i+4)] for i in starting_positions]
	return pattern in relevant_diagonal

# checks if the player who last played in the given column has won the game by doing so
def win(playing_board, column):
	row = playing_board.positions[column]-1
	player = playing_board.board[column][row]
	pattern = [player for i in range(4)]
	horizontal = pattern_horizontal(playing_board, column, row, pattern)
	vertical = pattern_vertical(playing_board, column, row, pattern)
	up_diagonal = pattern_upDiagonal(playing_board, column, row, pattern)
	down_diagonal = pattern_downDiagonal(playing_board, column, row, pattern)
	return horizontal or vertical or up_diagonal or down_diagonal





