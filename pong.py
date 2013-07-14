#!usr/bin python
#-*- coding:utf-8 -*-

import pygame
import pygame.display
from pygame.locals import *

class Pong:
	'''
		Coisas a fazer: sockets, bolinha, colisão, menu options
	'''
	barraTopo, barraChao = None, None	
	screen, divisoria, player1, player2, bola = None, None, None, None, None
	resolution, resoX, resoY, x, y = None, None, None, None, None

	def updateMenu(self):
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

		self.updateGame()

	def updateGame(self):
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
	
		self.updateMenu()

	def __init__(self):
		pygame.init()
		pygame.mixer.init()

		self.resolucao = pygame.display.list_modes(32)[0]
		self.screen = pygame.display.set_mode(self.resolucao, pygame.FULLSCREEN)
		self.resoX, self.resoY = self.resolucao[0], self.resolucao[1]
		
		pygame.display.set_caption('Pong - IEEE')
		pygame.display.flip()
		self.updateMenu()
		
if __name__ == '__main__':
	Pong()

