# main.py
# runs the Connect Four program (solves the game)
# J. Hassler Thurston
# Connect Four
# December 30, 2013

from board import *
from pattern import *
from sequence import *
from compute_moves import *

import time

# function that plays with a human
def play_human(human_player):
	# display a starting message
	print "Starting game of connect four..."
	# initialize the board
	board = Board(7,6)
	# alternate between querying a user for a move and moving
	while board.winner == 0:
		if board.turn == human_player:
			query_move(board)
		else:
			make_move(board)

# queries the user for a move
def query_move(playing_board):
	column = raw_input("Your turn. Please enter your move (an open column between 0 and " + str(playing_board.columns-1) + "):")
	playing_board.move(int(column))
	return True

# function that makes a move for the computer
def make_move(playing_board):
	# wait 2 seconds
	time.sleep(2)
	# make a move
	compute_move(playing_board)
	# print the move
	print "Computer moved in column " + str(playing_board.last_move)
	# wait .5 seconds
	time.sleep(.5)
	return True

# main function (for testing)
def main():
	board = Board(7,6)
	compute_move(board)
	print board.board

if __name__ == '__main__':
	play_human(1)












