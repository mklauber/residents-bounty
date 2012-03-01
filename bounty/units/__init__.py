from hexmap.Map import Map, MapUnit

class UnitError( Exception ): pass
class MovementError( UnitError ): pass

class Attribute( property ):
	pass

class Unit( object ):
	def __init__( self, *args, **keywords ):
		super( Unit, self ).__init__( *args, **keywords )
		self.max_health = 100
		self.health = 100
		self.movement = 3

	def reset_turn( self ):
		pass

	@Attribute
	def max_health( self ):		return self.get_max_health()
	def get_max_health( self ):	return self.max_health
	@Attribute
	def health( self ): 			return self.get_health()
	def get_health( self ):		return self.health
	@Attribute
	def movement( self ):			return self.get_movement()
	def get_movement( self ):	return self.movement

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

