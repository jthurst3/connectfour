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
	board.move(3)
	board.move(4)
	board.move(3)
	board.move(4)
	board.move(3)
	board.move(4)
	board.move(3)
	seq = Sequence(board, (3,0), 0)

if __name__ == '__main__':
	main()








