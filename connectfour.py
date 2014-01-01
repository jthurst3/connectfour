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

# function that plays with a human
def play_human():
	# display a starting message
	print "Starting game of connect four..."
	# query the user whether they want to go first or second
	human_player = int(raw_input("Do you want to go first or second? (Enter 1 or 2): "))
	# initialize the board
	board = Board(7,6)
	exit_status = 0
	while(exit_status == 0):
		game_play(board, human_player)
		take_back = int(raw_input("Press 1 to exit, or 0 to take back moves: "))
		if take_back == 1:
			exit_status = 1
		else:
			num_moves = int(raw_input("How many moves do you want to take back? "))
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
	column = int(raw_input("Your turn. Please enter your move (an open column between 1 and " + str(playing_board.columns) + ", 0 to take back moves): "))
	if column == 0:
		# we're taking back some moves
		num_moves = int(raw_input("How many moves do you want to take back? "))
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












