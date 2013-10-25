#!/usr/bin python

import os
import pygame
from pygame.locals import *

import Menu

class Main:
	def __init__(self):
		os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
		pygame.init()
		
		icon = pygame.image.load("Data/icon.png")
		pygame.display.set_icon(icon)

		resolution = pygame.display.list_modes(32)

		screen = pygame.display.set_mode(resolution[0], pygame.FULLSCREEN)
		resolution = (resolution[0][0], resolution[0][1])

		pygame.display.flip()
		pygame.mouse.set_visible(0)
		Menu.Update(screen, resolution[0], resolution[1])

if __name__ == "__main__":
	Pong()
	
