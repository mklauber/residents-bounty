from abc import ABCMeta, abstractmethod
from hexmap.Map import Map
from hexmap.Render import RenderGrid
import pygame
import random

from utilities import ExitError
import utilities

import logging
logger = logging.getLogger( __name__ )
class Screen( object ):

	__metaclass__ = ABCMeta

	def __init__( self, surface ):
		self.surface = surface
		self.clock = pygame.time.Clock()

	@abstractmethod
	def run( self ):
		pass

class TitleScreen( Screen ):

	def __init__( self, surface ):
		super( TitleScreen, self ).__init__( surface )
		self.map = Map( ( 20, 40 ) )
		self.grid = RenderGrid( self.map, radius=24 )

	def run( self ):
		#Leave it running until exit
		from pygame.locals import QUIT, MOUSEBUTTONDOWN

		x, y = 0, 0
		self.grid.draw()
		title = utilities.format_text( "Resident's\nBounty",
			font=pygame.font.SysFont( None, 72 ) )
		start = utilities.format_text( "Start" )
		start_box = []

		while True:
			new_x, new_y = ( 
				random.randint( 0, int( self.grid.width - self.surface.get_width() ) ),
				random.randint( 0, int( self.grid.height - self.surface.get_height() ) )
			)
			logger.debug( "Target: (%s, %s)", new_x, new_y )
			while ( x, y ) != ( new_x, new_y ) :

				for event in pygame.event.get():
					if event.type == QUIT:
						raise ExitError()
					if event.type == MOUSEBUTTONDOWN:
						if event.pos in start_box:
							return

				self.surface.fill( pygame.Color( 'grey' ) )

				# Make the background move
				x = x - 1 if new_x < x else x if new_x == x else x + 1
				y = y - 1 if new_y < y else y if new_y == y else y + 1
				self.surface.blit( self.grid, ( -x, -y ) )

				# Add the title text
				offset = utilities.center( self.surface, title )
				self.surface.blit( title, offset )

				# Add the start button
				top = offset[1] + title.get_height() + 50
				offset = utilities.center( self.surface, start )
				self.surface.blit( start, ( offset[0], top ) )
				# Update the start box location
				start_box = utilities.BoundingBox( offset[0], top, *start.get_size() )

				# Update the display
				pygame.display.update()
				self.clock.tick( 60 )
