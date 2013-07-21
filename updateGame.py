#!usr/bin python
#-*- coding:utf-8 -*-

import pygame
from pygame.locals import *

import updateMenu

class update:

	divisoria, player1, player2, bola = None, None, None, None
	resoX, resoY, x, y = None, None, None, None
	screen = None

	def __init__(self, _screen, _resoX, _resoY):
		self.screen = _screen
		self.resoX, self.resoY = _resoX, _resoY

		self.divisoria = pygame.Rect(self.resoX/2 - 5, 0, 10, self.resoY)
		self.player1 = pygame.Rect(10, (self.resoY/2 - self.resoY/5), self.resoX/90, self.resoY/5)
		self.player2 = pygame.Rect(self.resoX - 25, (self.resoY/2 - self.resoY/5), self.resoX/90, self.resoY/5)
		self.barraTopo = pygame.Rect(0, 0, self.resoX, 0)
		self.barraChao = pygame.Rect(0, self.resoY, self.resoX, 0)
		self.x, self.y = (self.resoX/2), (self.resoY/2)
		bola = pygame.draw.circle(self.screen, (0, 0, 255), (self.x, self.y), self.resoX/120)

		while 1:
			self.screen.fill((0, 0, 0))

			# Eventos
			keys = pygame.key.get_pressed()
			
			if keys[K_ESCAPE]: break
			elif keys[K_DOWN]:
				if self.player1.y <= (self.resoY - self.resoY/5 - 5):
					self.player1.move_ip(0, 1)
			elif keys[K_UP]: 
				if self.player1.y >= 5:
					self.player1.move_ip(0, -1)

			for event in pygame.event.get():
				if event.type == QUIT: break
			# ---

			
			
			# Área de desenho:
			pygame.draw.rect(self.screen, (255, 255, 255), self.divisoria)
			pygame.draw.rect(self.screen, (255, 255, 255), self.player1)
			pygame.draw.rect(self.screen, (255, 255, 255), self.player2)
			pygame.draw.rect(self.screen, (255, 255, 255), self.barraTopo)
			pygame.draw.rect(self.screen, (255, 255, 255), self.barraChao)
			
			bola = pygame.draw.circle(self.screen, (0, 0, 255), (self.x, self.y), self.resoX/120)
			# ---
		
			pygame.display.flip()
	
		updateMenu.update(self.screen, self.resoX, self.resoY)
