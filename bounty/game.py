class Game( object ):

	def __init__( self, map ):
		self.map = map
		self.turn = 0

	def turn( self ):
		"""
		Increment the turn count, and reset any turn specific values
		"""
		self.turn += 1
		for position, unit in self.map.units.items():
			unit.movement = unit.max_movement
