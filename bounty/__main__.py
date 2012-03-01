from screens import TitleScreen
from utilities import ExitError
import pygame
import random

import logging
logger = logging.getLogger()

class Game( object ):

	def __init__( self ):
		self.window = pygame.display.set_mode( ( 640, 480 ), 1 )
		self.screens = [ TitleScreen ]


	def run( self ):
		while self.screens:
			screen = self.screens.pop( 0 )( self.window )
			screen.run()

try:
	logging.basicConfig( level=logging.DEBUG )
	pygame.init()
	game = Game()
	game.run()
except ExitError as e:
	pass
finally:
	pygame.quit()
