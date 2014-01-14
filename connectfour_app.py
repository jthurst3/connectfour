# app.py
# runs connectfour program with Flask
# J. Hassler Thurston
# Personal website
# 12 January 2014

from flask import Flask, request, jsonify, abort, make_response
import board, compute_moves
app = Flask(__name__)

# error handling
# responses modified from http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)
@app.errorhandler(405)
def not_allowed(error):
    return make_response(jsonify( { 'error': 'Method not allowed' } ), 405)
@app.errorhandler(500)
def internal_error(error):
	return make_response(jsonify( { 'error': 'Internal server error' } ), 500)


# JSON requests should be in this form:
# {
# 	'columns': number of columns,
# 	'rows': number of rows,
# 	'moves': array of all previous moves
# }

@app.route('/move', methods = ['GET'])
def make_move():
	# check to see if JSON exists
	if not request.json:
		abort(400)
	# check to see if JSON is in the right format
	if not checkJSON(request.json):
		abort(400)

	# if it is, define a variable to keep track of whether the computations ran successfully
	successful = True
	# create a new playing board
	playing_board = board.Board(request.json['columns'], request.json['rows'])
	# and check to see if it initialized correctly
	if not playing_board.successfulInit:
		successful = False
	# initialize it with the previous moves
	if successful:
		successful = playing_board.move_sequence(request.json['moves'])
	# make another move
	if successful:
		successful = compute_moves.compute_move(playing_board)

	# if everything went well, return a JSON to the correct URL
	if successful:
		return jsonify(toJSON(playing_board))
	else: abort(500)

# converts the current state of the playing board to JSON format, to be returned to the client
def toJSON(playing_board):
	columns = playing_board.columns
	rows = playing_board.rows
	moves = playing_board.move_history
	json = {
		'columns': columns,
		'rows': rows,
		'moves': moves
	}
	return json

# checks to see if JSON from client is in the correct format
def checkJSON(json):
	# rows, columns, and moves fields must exist
	if not 'columns' in request.json or not 'rows' in request.json or not 'moves' in request.json:
		return False
	# rows and columns must be integers
	if not isinstance(request.json['columns'], int) or not isinstance(request.json['rows'], int):
		return False
	# rows and columns must be > 4
	if request.json['columns'] < 4 or request.json['rows'] < 4:
		return False
	# to not overload the server, rows and columns must be < 15
	if request.json['columns'] > 15 or request.json['rows'] > 15:
		return False
	# moves must be a list
	if not isinstance(request.json['moves'], list):
		return False
	# every move must be an integer
	if not all(isinstance(move, int) for move in request.json['moves']):
		return False
	# if all this is satisfied, JSON is in the correct format
	return True

if __name__ == '__main__':
	# MAKE SURE TO NOT HAVE debug=True WHEN PUSHING TO PRODUCTION
	app.run()





