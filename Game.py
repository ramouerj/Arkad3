#!/usr/bin python

import pygame
from pygame.locals import *

import time

import Menu, Communication

class Update:

	Com = Communication.Update()

	def __init__(self, screen, resolution_x, resolution_y):
		WHITE, RED = (255, 255, 255), (255, 0, 0)

		scores = [0, 0]
		font = pygame.font.Font("data/font.TTF", 30)

		bar_rect = [pygame.Rect(0, 00, resolution_x, 10), pygame.Rect(0, resolution_y - 11, resolution_x, 11),
						pygame.Rect(resolution_x/2, 0, 10, resolution_y)]

		player_rect = [pygame.Rect(10, (3.9*resolution_y/10), resolution_x/90, resolution_y/5),
						pygame.Rect(resolution_x - 25, (3.9*resolution_y/10), resolution_x/90, resolution_y/5)]

		circle_width = resolution_x/70
		circle_x, circle_y = resolution_x/2 - circle_width, resolution_y/2 - circle_width
		speed_x, speed_y, speed_circ = resolution_y/2, resolution_y/2, resolution_y/2

		self.Com.isAlive = True
		self.Com.start()

		time.sleep(5)
		
		while True and self.Com.isAlive:
			time_passed = pygame.time.Clock().tick(35)
			time_sec = time_passed / 1000.
			screen.fill((0, 0, 0))

			keys = pygame.key.get_pressed()
			if keys[K_ESCAPE]:
				self.Com.isAlive = False
				Menu.Update(screen, resolution_x, resolution_y)
				break

			for event in pygame.event.get(): 
				if event.type == QUIT:
					break

			if int(self.Com.players) == 1:
				player_rect[0].y += self.Com.mv_p1y/1.5
			else:
				player_rect[0].y += self.Com.mv_p1y/1.5
				player_rect[1].y += self.Com.mv_p2y/1.5

			circle_x += speed_x * time_sec
			circle_y += speed_y * time_sec
			ia_speed = speed_circ * time_sec

			if circle_y <= circle_width + 10.:
				speed_y = -speed_y
			if circle_y >= resolution_y - circle_width - 10.:
				speed_y = -speed_y
			
			for player in player_rect:
				if player.y <= 11.: 
					player.y = 10.
				if player.y >= resolution_y - player.height - 5.:
					player.y = resolution_y - player.height - 5.

			if int(self.Com.players) == 1:
				if circle_x >= resolution_x/2:
					if not player_rect[1].y == circle_y + circle_width:
						if player_rect[1].y + player_rect[1].height/2 < circle_y + circle_width:
							player_rect[1].y += ia_speed
						if player_rect[1].y > circle_y - player_rect[1].height/2:
							player_rect[1].y -= ia_speed
					else:
						player_rect[1] == circle_y + circle_width

			if circle_x <= player_rect[0].x + circle_width + 10:
				if circle_y >= player_rect[0].y and circle_y <= player_rect[0].y + player_rect[0].height:
					speed_x = -speed_x
			if circle_x >= player_rect[1].x - circle_width + 10:
					if circle_y >= player_rect[1].y and circle_y <= player_rect[1].y + player_rect[1].height:
						speed_x = -speed_x

			if circle_x > resolution_x:
				circle_x, circle_y = resolution_x/2 - circle_width, resolution_y/2 - circle_width
				speed_x = -speed_x
				scores[1] += 1
			if circle_x < 0:
				circle_x, circle_y = resolution_x/2 - circle_width, resolution_y/2 - circle_width
				speed_x = -speed_x
				scores[0] += 1

			for bar in bar_rect:
				pygame.draw.rect(screen, WHITE, bar)
			for player in player_rect:
				pygame.draw.rect(screen, WHITE, player)
			pygame.draw.circle(screen, RED, (int(circle_x), int(circle_y)), circle_width/2)

			s1, s2 = font.render(str(scores[0]), 1, WHITE), font.render(str(scores[1]), 1, WHITE)
			screen.blit(s1, (resolution_x/2 + font.size(str(scores[0]))[0], 15))
			screen.blit(s2, (resolution_x/2 - font.size(str(scores[1]))[0] - 14, 15))

			pygame.display.flip()