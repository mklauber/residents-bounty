from pygame import Color
import pygame
import logging
logger = logging.getLogger( __name__ )


class BoundingBox( object ):
	"""
	A bounding box that implements the __contains__ method for checking if mouse
	clicks are in a given area.
	"""
	def __init__( self, left, top, width, height ):
		self.top = top
		self.left = left
		self.width = width
		self.height = height

	def __str__( self ):
		return "Top: %s, Left: %s, width: %s, height: %s" % ( 
			self.top, self.left, self.width, self.height )

	def __contains__( self, item ):
		if item[0] < self.left or self.left + self.width < item[0]:
			return False
		if item[1] < self.top or self.top + self.height < item[1]:
			return False
		return True



def format_text( text, font=None, foreground=None, background=None ):
	BLACK = pygame.Color( 0, 0, 0 )
	if font == None: font = pygame.font.SysFont( None, 48 )

	#Calculate size of alert box
	lines = text.split( '\n' )
	widths, heights = zip( *[font.size( line ) for line in lines ] )
	width, height = max( widths ), sum( heights )

	#Create alert box
	alert = pygame.Surface( ( width, height ) )

	if background == None:
		background = pygame.Color( 255, 0, 255 )
		alert.set_colorkey( background )
		alert.fill( background )
	else:
		background = pygame.Color( 0, 0, 0, 255 )
	if not foreground: foreground = pygame.Color( 'white' )


	logger.debug( "Alert size: %s", alert.get_size() )

	for i, line in enumerate( lines ) :
		logger.debug( "Line: %s, width:%s", line, font.size( line )[0] )
		offset = ( width - font.size( line )[0] ) / 2
		alert.blit( 
			font.render( line, False, foreground, background ),
			( offset, i * font.get_height() )
		)

	#alert = font.render( text, True, WHITE, BLACK )
	return alert

def center( parent, child ):
	if isinstance( parent, pygame.Surface ):
		parent = parent.get_size()
	if isinstance( child, pygame.Surface ):
		child = child.get_size()

	top = ( parent[1] - child[1] ) / 2
	left = ( parent[0] - child[0] ) / 2

	return ( left, top )
