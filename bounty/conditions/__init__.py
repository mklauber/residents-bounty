from abc import ABCMeta, abstractmethod

class Condition( object ):

	__metaclass__ = ABCMeta

	def __init__( self, unit, duration=2 ):

		self.duration = duration
		self.unit = unit
		self.count = 0
		self.add()

	@abstractmethod
	def add( self ):
		self.unit.conditions.append( self )

	@abstractmethod
	def remove( self ):
		self.unit.conditions.remove( self )

	@property
	def expired( self ):
		return self.count >= self.duration

	def bind( self, function, transformation ):
		values = {'f' : function }
		def result():
			if not self.expired:
				self.count += 1
				return transformation( values['f']() )
			else:
				self.remove()
				return values['f']()
		result.values = values
		result.expired = self.expired
		self.function = result
		return result

	def unbind( self, function ):
		if function == self.function:
			function = self.function.values['f']
		else:
			while function.values['f'] != self.function and hasattr( function, 'values' ):
				function = function.values['f']
			function.values['f'] = function.values['f'].values['f']

		return function

class Slow( Condition ):

	def add( self ):
		super( Slow, self ).add()

		unit = self.unit
		unit._distance = self.bind( unit._distance, lambda x: x - 2 )

	def remove( self ):
		super( Slow, self ).remove()

		unit = self.unit
		unit._distance = self.unbind( unit._distance )



















