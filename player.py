class Player:
	WHITE = 1
	BLACK = 0
	
	def __init__(self, player_id):
		self._id = player_id
		if player_id == 0: # black
			self.direction = 1
			self.name = "Black"
		else: # white
			self.direction = -1
			self.name = "White"

	# TODO: for now make it stdin or something, later we can decide with AI
	# prompts player to make a move as it is his turn to play
	def makeMove(board):
		print("Player {} ({}) will make a move".format(self._id, self.name))
		board.makeMove(self, Pos(1,1), Pos(2,1))
