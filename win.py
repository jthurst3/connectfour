# win.py
# checks to see if one player has won the game
# J. Hassler Thurston
# Connect Four
# December 30, 2013

# checks to see if the player who played in the given column has won the game
def win(playing_board, column):
	# if nobody has played in the column, return false trivially
	if(playing_board.positions[column] == 0):
		return False
	# otherwise, get the player who could win
	player = playing_board.board[column][playing_board.positions[column] - 1]
	# We need to check for a win horizontally, vertically, and along the diagonals.
	horizontal = winHorizontal(playing_board, column, player)
	vertical = winVertical(playing_board, column, player)
	up_diagonal = winUpDiagonal(playing_board, column, player)
	down_diagonal = winDownDiagonal(playing_board, column, player)
	return horizontal or vertical or up_diagonal or down_diagonal

# Vertical check
def winVertical(playing_board, column, player):
	if(playing_board.positions[column] < 4):
		return False
	relevant_chips = playing_board.board[column][-4:]
	return relevant_chips == [player,player,player,player]
# Horizontal check
def winHorizontal(playing_board, column, player):
	row = playing_board.positions[column] - 1
	min_starting_column = max(0, column-3)
	max_starting_column = min(column, playing_board.columns-4)
	relevant_chips_array = [[playing_board.board[j][row] for j in range(i,i+4)] 
		for i in range(min_starting_column,max_starting_column+1)]
	return [player,player,player,player] in relevant_chips_array
# up diagonal check (diagonal whose row increases with an increase in column)
def winUpDiagonal(playing_board, column, player):
	row = playing_board.positions[column] - 1
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
	return [player,player,player,player] in relevant_chips_array
# down diagonal check (diagonal whose row decreases with an increase in column)
def winDownDiagonal(playing_board, column, player):
	row = playing_board.positions[column] - 1
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
	return [player,player,player,player] in relevant_diagonal





