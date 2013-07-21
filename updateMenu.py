#!usr/bin python
#-*- coding:utf-8 -*-

import pygame
from pygame.locals import *

import updateGame

class update:

	screen, resoX, resoY = None, None, None

	def __init__(self, _screen, _resoX, _resoY):
		self.screen = _screen
		self.resoX, self.resoY = _resoX, _resoY

		fonte = pygame.font.Font('data/font.TTF', 30)
		opcao1, opcao2, opcao3, arcade = None, None, None, None
		escolha = [True, False, False]
		cor = [(255, 255, 255), (255, 255, 255), (255, 255, 255)]

		logoIeee = pygame.image.load('data/logo.png')
		logoIeeeRect = pygame.Rect(self.resoX/2 - logoIeee.get_height() + 15,
 					   self.resoY/2 - logoIeee.get_width() + self.resoY/2,
					   logoIeee.get_height(), logoIeee.get_width())

		while 1:
			self.screen.fill((0, 0, 0))
			
			keys = pygame.key.get_pressed()			
			pygame.time.delay(90)

			if keys[K_RETURN]:
				if escolha[0]:
					pygame.mixer.music.load('data/pong_menu_sound.mp3')
					pygame.mixer.music.play()
					while pygame.mixer.music.get_busy(): pass
					break
				elif escolha[1]:
					pass # FOCO: não esquecer o menu de opções
				elif escolha[2]:
					exit()
			elif keys[K_DOWN]:
				if escolha[0]:
					escolha = [False, True, False]
				elif escolha[1]:
					escolha = [False, False, True]
			elif keys[K_UP]:
				if escolha[2]:
					escolha = [False, True, False]
				elif escolha[1]:
					escolha = [True, False, False]

			if   escolha[0]: cor = [(152, 251, 152), (255, 255, 255), (255, 255, 255)]
			elif escolha[1]: cor = [(255, 255, 255), (152, 251, 152), (255, 255, 255)]
			elif escolha[2]: cor = [(255, 255, 255), (255, 255, 255), (152, 251, 152)]
			
			for event in pygame.event.get():
				if event.type == QUIT: exit()

			opcao1 = fonte.render("PONG!", 1, cor[0])
			opcao2 = fonte.render("Options", 1, cor[1])
			opcao3 = fonte.render("Exit", 1, cor[2])
			
			self.screen.blit(opcao1, (self.resoX/2 - fonte.size("PONG!")[0]/2, self.resoY/2 - fonte.size("PONG!")[1]/2 - 50))
			self.screen.blit(opcao2, (self.resoX/2 - fonte.size("Options")[0]/2, self.resoY/2 - fonte.size("Options")[1]/2))
			self.screen.blit(opcao3, (self.resoX/2 - fonte.size("Exit")[0]/2, self.resoY/2 - fonte.size("Exit")[1]/2 + 50))
			self.screen.blit(logoIeee, logoIeeeRect)
			pygame.display.flip()

		updateGame.update(self.screen, self.resoX, self.resoY)