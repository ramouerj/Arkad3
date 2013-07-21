#!usr/bin python
#-*- coding:utf-8 -*-

import pygame
import pygame.display
from pygame.locals import *

import updateMenu

class Pong:
	# Coisas a fazer: sockets, bolinha, colisão, menu options	
	screen, resolucao, resoX, resoY = None, None, None, None

	def __init__(self):
		pygame.init()
		pygame.mixer.init()

		self.resolucao = pygame.display.list_modes(32)[0]
		self.screen = pygame.display.set_mode(self.resolucao, pygame.FULLSCREEN)
		self.resoX, self.resoY = self.resolucao[0], self.resolucao[1]
		
		pygame.display.set_caption('Pong - IEEE')
		pygame.display.flip()
		updateMenu.update(self.screen, self.resoX, self.resoY)
		
if __name__ == '__main__':
	Pong()

