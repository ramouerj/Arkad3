#!/usr/bin python

import pygame
import Menu
import Game
from pygame.locals import *

class Update:

	def run(self):
		while True:
			pygame.time.Clock().tick(35)
			self.screen.fill((0, 0, 0))

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					break

			keys = pygame.key.get_pressed()
			pygame.time.delay(35)
			if keys[K_DOWN] and self.colors[2] != self.green:
				self.colors[self.colors.index(self.green) + 1] = self.green
				self.colors[self.colors.index(self.green)] = self.white
			elif keys[K_UP] and self.colors[0] != self.green:
				self.colors[self.colors.index(self.green) - 1] = self.green
				self.colors[self.colors.index(self.green) + 1] = self.white
			elif keys[K_ESCAPE]:
				Menu.Update(self.screen, self.resolution_x, self.resolution_y)
				break
			elif keys[K_RETURN]:
				if self.colors[0] == self.green:
					Game.Update(self.screen, self.resolution_x, self.resolution_y, 0)
					break
				if self.colors[1] == self.green:
					Game.Update(self.screen, self.resolution_x, self.resolution_y, 1)
					break
				if self.colors[2] == self.green:
					Game.Update(self.screen, self.resolution_x, self.resolution_y, 2)
					break

			self.draw()

	def draw(self):
		for index in range(0, 3):
			self.option = self.font.render(self.options[index], 1, self.colors[index])
			self.screen.blit(self.option, (self.resolution_x/2 - self.font.size(self.options[index])[0]/2,
							 self.resolution_y/2 - self.font.size(self.options[index])[1]/2 + index*40 - 60))
		pygame.display.flip()

	def __init__(self, screen, resolution_x, resolution_y):
		self.screen = screen
		self.resolution_x = resolution_x
		self.resolution_y = resolution_y

		self.font = pygame.font.Font("Data/font.TTF", 30)
		self.options = ["Player 1 vs CPU", "Player 1 vs Player 2", "IEEE Mode"]
		self.white = (250, 250, 250)
		self.green = (152, 251, 152)
		self.colors = [self.green, self.white, self.white]

		self.run()