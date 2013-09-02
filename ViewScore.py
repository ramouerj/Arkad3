#!/usr/bin python

import pygame
from pygame.locals import *

class Update:
	def __init__(self, screen, resolution_x, resolution_y):
		pygame.time.Clock().tick(35)
		screen.fill((0, 0, 0))

		keys = pygame.key.get_pressed()
		if keys[K_ESCAPE]:
			Menu.Update(screen, resolution_x, resolution_y)
			break
		for event in pygame.event.get():
			if event.type == QUIT: break