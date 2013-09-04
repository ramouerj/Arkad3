#!/usr/bin python

import pygame
from pygame.locals import *

class ViewUpdate:
	def __init__(self, screen, resolution_x, resolution_y):
		while True:
			pygame.time.Clock().tick(35)
			screen.fill((0, 0, 0))

			keys = pygame.key.get_pressed()
			if keys[K_ESCAPE]: break

			for event in pygame.event.get():
				if event.type == QUIT:
					break

			pygame.display.flip()

class SaveUpdate:
	def __init__(self):
		pass