from hexmap.Map import Map, MapUnit

class UnitError( Exception ): pass
class MovementError( UnitError ): pass

class Unit( object ):
	def __init__( self, *args, **keywords ):
		super( Unit, self ).__init__( *args, **keywords )
		self.max_health = 100
		self.health = 100
		self.max_movement = 6
		self.movement = 6

	def move( self, target ):
		distance = Map.distance( self.position, target )
		if distance > self.movement:
			raise MovementError()

		self.position = target
		self.movement -= distance
		return self.movement

	def heal( self, amount ):
		healed = max( amount, self.max_health - self.health )
		self.health = min( self.health + amount, self.max_health )
		return healed

class Character( Unit, MapUnit ):

	def __init__( self, *args, **keyword ):
		super( Character, self ).__init__( *args, **keywords )
		self.attacks = {}
		self.items = []
		self.health = 100

	def paint( self, surface ):
		return surface

class NPC( Unit, MapUnit ):
	def __init__( self, *args, **keywords ):
		super( NPC, self ).__init__( *args, **keywords )

	def paint( self, surface ):
		return surface

