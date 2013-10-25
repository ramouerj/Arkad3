#!/usr/bin python

import pygame
from pygame.locals import *

import Modules.Database
import Menu

class ViewUpdate:

	def run(self):
		while True:
			pygame.time.Clock().tick(35)
			self.screen.fill((0, 0, 0))

			for event in pygame.event.get():
				if event.type == QUIT:
					break

			keys = pygame.key.get_pressed()
			if keys[K_ESCAPE]: 
				Menu.Update(self.screen, self.resolution_x, self.resolution_y)
				break

			self.draw()

	def draw(self):
		if self.scores:
			if len(self.scores) <= 5:
				for index in range(1, len(self.scores)):
					data = str("%s vs %s %s|%s") % (str(self.scores[index][1]), str(self.scores[index][2]), str(self.scores[index][3]), str(self.scores[index][4]))
					score = self.font.render(data, 1, (250, 250, 250))
					self.screen.blit(score, (self.resolution_x/2 - self.font.size(str(score))[0]/2 + 60,
									 self.resolution_y/2 - self.font.size(str(score))[1]/2 + index*40 - 60))
			else:
				for index in range(1, 5):
						data = str("%s vs %s %s|%s") % (str(self.scores[index][1]), str(self.scores[index][2]), str(self.scores[index][3]), str(self.scores[index][4]))
						score = self.font.render(data, 1, (250, 250, 250))
						self.screen.blit(score, (self.resolution_x/2 - self.font.size(str(score))[0]/2 + 60,
										 self.resolution_y/2 - self.font.size(str(score))[1]/2 + index*40 - 60))
		else:
			msg = "No data"
			score = self.font.render(msg, 1, (250, 250, 250))
			self.screen.blit(score, (self.resolution_x/2 - self.font.size(msg)[0]/2,
							 self.resolution_y/2 - self.font.size(msg)[1]/2))
		pygame.display.flip()

	def __init__(self, screen, resolution_x, resolution_y):
		self.screen = screen
		self.resolution_x = resolution_x
		self.resolution_y = resolution_y

		self.font = pygame.font.Font("Data/font.TTF", 30)
		self.scores = Modules.Database.Database().seekASC()

		self.run()

class SaveUpdate:

	def run(self):
		while self.isAlive:
			pygame.time.Clock().tick(35)
			self.screen.fill((0, 0, 0))

			for event in pygame.event.get():
				if event.type == QUIT:
					self.isAlive = False

			self.draw()

	def keys(self):
		keys = pygame.key.get_pressed()
		'''
		elif keys[K_RETURN]:
			self.isAlive = False
		else:
			for key in keys:
				if key != 0:
					return key
		'''

	def draw(self):
		pygame.display.flip()

	def __init__(self, screen, resolution_x, resolution_y):
		self.screen = screen
		self.resolution_x = resolution_x
		self.resolution_y = resolution_y

		self.isAlive = True

		self.run()