# connectfour.py
# runs the Connect Four program (makes the game interactive)
# J. Hassler Thurston
# Connect Four
# December 30, 2013

from board import *
from pattern import *
from sequence import *
from compute_moves import *

import time

# checks to see if user entered a valid integer
# from http://stackoverflow.com/questions/1265665/python-check-if-a-string-represents-an-int-without-using-try-except
def getInt(input_arg):
	try:
		user_input = raw_input(input_arg)
		return int(user_input)
	except ValueError:
		print "Did not enter a valid integer."
		return getInt(input_arg)

# function that plays with a human
def play_human():
	# display a starting message
	print "Starting game of connect four..."
	# query the user whether they want to go first or second
	human_player = getInt("Do you want to go first or second? (Enter 1 or 2): ")
	# initialize the board
	board = Board(7,6)
	exit_status = 0
	while(exit_status == 0):
		game_play(board, human_player)
		take_back = getInt("Press 1 to exit, or 0 to take back moves: ")
		if take_back == 1:
			exit_status = 1
		else:
			num_moves = getInt("How many moves do you want to take back? ")
			board.take_back_moves(num_moves)


# main stage of playing the game
def game_play(playing_board, human_player):
	# alternate between querying a user for a move and moving
	while playing_board.winner == 0:
		if playing_board.turn == human_player:
			query_move(playing_board)
		else:
			make_move(playing_board)

# queries the user for a move
def query_move(playing_board):
	column = getInt("Your turn. Please enter your move (an open column between 1 and " + str(playing_board.columns) + ", 0 to take back moves): ")
	if column == 0:
		# we're taking back some moves
		num_moves = getInt("How many moves do you want to take back? ")
		playing_board.take_back_moves(num_moves)
		return True
	playing_board.move(column-1)
	return True

# function that makes a move for the computer
def make_move(playing_board):
	# wait 2 seconds
	time.sleep(1)
	# make a move
	compute_move(playing_board)
	# print the move
	print "Computer moved in column " + str(playing_board.move_history[-1]+1)
	# wait .5 seconds
	time.sleep(.5)
	return True

# main function (for testing)
def main():
	board = Board(7,6)
	compute_move(board)
	print board.board

if __name__ == '__main__':
	play_human()












