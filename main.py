# main.py
# runs the Connect Four program (solves the game)
# J. Hassler Thurston
# Connect Four
# December 30, 2013

from board import *
# from win import *
from pattern import *
from sequence import *

def bestMove(player):
	pass

def main():
	board = Board(7,6)
	board.move_sequence([3,4,4,3,3,4,5,2,2,4,3,4,4,3,0,1,1,2])
	print board.winning_squares

if __name__ == '__main__':
	main()








