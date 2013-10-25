#!/usr/bin python 

import pygame
from pygame.locals import *
import Score
import Game
import Players

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
			if keys[K_DOWN] and self.colors[3] != self.green:
				self.colors[self.colors.index(self.green) + 1] = self.green
				self.colors[self.colors.index(self.green)] = self.white
			elif keys[K_UP] and self.colors[0] != self.green:
				self.colors[self.colors.index(self.green) - 1] = self.green
				self.colors[self.colors.index(self.green) + 1] = self.white
			elif keys[K_RETURN]:
				if self.colors[0] == self.green:
					self.flush_input()
					Players.Update(self.screen, self.resolution_x, self.resolution_y)
					break
				if self.colors[1] == self.green:
					Score.ViewUpdate(self.screen, self.resolution_x, self.resolution_y)
					break
				if self.colors[2] == self.green: pass
				if self.colors[3] == self.green: exit()

			self.draw()

	def flush_input(self):
		import sys
		sys.stdin.flush()

	def draw(self):
		for index in range(0, 4):
			self.option = self.font.render(self.options[index], 1, self.colors[index])
			self.screen.blit(self.option, (self.resolution_x/2 - self.font.size(self.options[index])[0]/2,
				self.resolution_y/2 - self.font.size(self.options[index])[1]/2 + index*40 - 60))

		self.screen.blit(self.logoIeee, self.logoIeeeRect)
		pygame.display.flip()

	def __init__(self, screen, resolution_x, resolution_y):
		self.screen = screen
		self.resolution_x = resolution_x
		self.resolution_y = resolution_y

		self.font = pygame.font.Font("Data/font.TTF", 30)
		self.options = ["Pong!", "Score", "Options", "Exit"]
		self.white = (250, 250, 250)
		self.green = (152, 251, 152)
		self.colors = [self.green, self.white, self.white, self.white]

		self.logoIeee = pygame.image.load("Data/logo.png")
		self.logoIeeeRect = pygame.Rect(self.resolution_x/2 - self.logoIeee.get_height() + 15,
										self.resolution_y/2 - self.logoIeee.get_width() + self.resolution_y/2,
										self.logoIeee.get_height(), self.logoIeee.get_width())
		self.run()