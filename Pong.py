#!/usr/bin python

import pygame
from pygame.locals import *

import Menu

class Pong:
	def __init__(self):
		pygame.init()

		resolution = pygame.display.list_modes(32)
		screen = pygame.display.set_mode(resolution[0], pygame.FULLSCREEN)
		resolution = (resolution[0][0], resolution[0][1])

		pygame.display.flip()
		pygame.mouse.set_visible(0)
		Menu.Update(screen, resolution[0], resolution[1])

if __name__ == "__main__":
	Pong()