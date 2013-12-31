# main.py
# runs the Connect Four program (solves the game)
# J. Hassler Thurston
# Connect Four
# December 30, 2013

from board import *
# from win import *
from pattern import *

def bestMove(player):
	pass

def main():
	board = Board(6,7)
	board.move(3)
	board.move(4)
	board.move(4)
	board.move(4)
	board.move(4)
	board.move(4)
	board.move(4)
	board.move(4)
	board.move(3)
	board.move(2)
	board.move(2)
	board.move(1)
	board.move(1)
	board.move(0)
	print board.board

if __name__ == '__main__':
	main()








