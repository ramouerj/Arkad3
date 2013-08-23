#!/usr/bin python

import pygame
from pygame.locals import *

import Menu

class Update:
# --Constructor
	def __init__(self, screen, resolution_x, resolution_y):
# Colors
		WHITE, RED = (255, 255, 255), (255, 0, 0)
# score = [player1_score, player2_score]
		scores = [0, 0]
		font = pygame.font.Font("data/font.TTF", 30)
# bar_rect = [top, button, division]
		bar_rect = [pygame.Rect(0, 00, resolution_x, 10), pygame.Rect(0, resolution_y - 11, resolution_x, 11),
						pygame.Rect(resolution_x/2, 0, 10, resolution_y)]
# player_rect = [player_rect1, player_rect2]
		player_rect = [pygame.Rect(10, (3.9*resolution_y/10), resolution_x/90, resolution_y/5),
						pygame.Rect(resolution_x - 25, (3.9*resolution_y/10), resolution_x/90, resolution_y/5)]
# Circle: rect, position and speed
		circle_width = resolution_x/70
		circle_x, circle_y = resolution_x/2 - circle_width, resolution_y/2 - circle_width
		speed_x, speed_y, speed_circ = 300., 300., 300.
# Loop
		while True:
			time_passed = pygame.time.Clock().tick(35)
			time_sec = time_passed / 1000.
			screen.fill((0, 0, 0))
# Event keys
			keys = pygame.key.get_pressed()
			if keys[K_ESCAPE]:
				Menu.Update(screen, resolution_x, resolution_y)
				break
			if keys[K_UP] and player_rect[0].y >= 11: 
				player_rect[0].move_ip(0, -(.5 - time_sec)/time_sec)
	# arduino:  if keys[K_UP]: player_rect[0].move_ip(0, -(left - time_sec)/time_sec)
			if keys[K_DOWN] and player_rect[0].y <= resolution_y - player_rect[0].height - 5: 
				player_rect[0].move_ip(0, (.5 - time_sec)/time_sec)
	# arduino:  if keys[K_UP]: player_rect[0].move_ip(0, (right - time_sec)/time_sec)
			for event in pygame.event.get():
					if event.type == QUIT: break
# Moviment of circle
			circle_x += speed_x * time_sec
			circle_y += speed_y * time_sec
# Collide events
	# In bars
			if circle_y <= circle_width/2 + 10.:
				speed_y = -speed_y
			if circle_y >= resolution_y - circle_width/2 - 10.:
				speed_y = -speed_y
	# In players
			player_rect[1].y = pygame.mouse.get_pos()[1]
			if circle_x <= player_rect[0].x + circle_width/2 + 10:
				if circle_y >= player_rect[0].y and circle_y <= player_rect[0].y + player_rect[0].height:
					speed_x = -speed_x
			if circle_x >= player_rect[1].x + circle_width/2 - 10:
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
# Draw bars, players and circle
			for bar in bar_rect:
				pygame.draw.rect(screen, WHITE, bar)
			for player in player_rect:
				pygame.draw.rect(screen, WHITE, player)
			pygame.draw.circle(screen, RED, (int(circle_x), int(circle_y)), circle_width/2)
# Draw scores
			s1, s2 = font.render(str(scores[0]), 1, WHITE), font.render(str(scores[1]), 1, WHITE)
			screen.blit(s1, (resolution_x/2 + font.size(str(scores[0]))[0], 15))
			screen.blit(s2, (resolution_x/2 - font.size(str(scores[1]))[0] - 14, 15))

			pygame.display.flip()