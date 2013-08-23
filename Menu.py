#!/usr/bin python

import pygame
from pygame.locals import *

import Game

class Update:
	def __init__(self, screen, resolution_x, resolution_y):
		font = pygame.font.Font("data/font.TTF", 30)
		options = ["Pong!", "Score", "Options", "Exit"]
		white, green = (255, 255, 255), (152, 251, 152)
		colors = [green, white, white, white]

		logoIeee = pygame.image.load('data/logo.png')
		logoIeeeRect = pygame.Rect(resolution_x/2 - logoIeee.get_height() + 15,
 					   resolution_y/2 - logoIeee.get_width() + resolution_y/2,
					   logoIeee.get_height(), logoIeee.get_width())
		while True:
			pygame.time.Clock().tick(35)
			screen.fill((0, 0, 0))
# Events
			keys = pygame.key.get_pressed()
			pygame.time.delay(90)
			if keys[K_DOWN] and (colors[3] != green): 
				colors[colors.index(green) + 1] = green
				colors[colors.index(green)] = white
			elif keys[K_UP] and (colors[0] != green):
				colors[colors.index(green) - 1] = green
				colors[colors.index(green) + 1] = white
			elif keys[K_RETURN]:
				if colors[0] == green: Game.Update(screen, resolution_x, resolution_y); break;
				if colors[1] == green: pass
				if colors[2] == green: pass
				if colors[3] == green: exit()
			for event in pygame.event.get():
				if event.type == QUIT: break
# Draw Font
			for index in range(0, 4):
				option = font.render(options[index], 1, colors[index])
				screen.blit(option, (resolution_x/2 - font.size(options[index])[0]/2,
					resolution_y/2 - font.size(options[index])[1]/2 + index*40 - 60))
# Draw Logo
			screen.blit(logoIeee, logoIeeeRect)

			pygame.display.flip()
		