#!/usr/bin python

import pygame
import time
import Menu
import Device
from pygame.locals import *

class Update:

	def run(self):
		self.connection.start()
		while self.connection.isAlive:

			self.time_passed = pygame.time.Clock().tick(35)
			self.time_sec = self.time_passed/1000.

			for event in pygame.event.get():
				if event.type == QUIT:
					break

			self.screen.fill((0, 0, 0))

			keys = pygame.key.get_pressed()
			if keys[K_ESCAPE]:
				self.connection.stop()
				Menu.Update(self.screen, self.resolution_x, self.resolution_y)

			self.draw()
	
	def detect_players(self):
			count = 0
			for i in range(0, 10):
				if self.connection.players == 2:
					count += 1
			if count >= 10: return 2
			else: return 1

	def draw(self):
		self.move_players()
		self.move_circle()
		self.collisions()

		for bar in self.bar_rects:
			pygame.draw.rect(self.screen, self.white, bar)
		for player in self.player_rects:
			pygame.draw.rect(self.screen, self.white, player)

		pygame.draw.circle(self.screen, self.red, (int(self.circle_x), int(self.circle_y)), self.circle_width/2)

		p1_score = self.font.render(str(self.score[0]), 1, self.white)
		p2_score = self.font.render(str(self.score[1]), 1, self.white)
		self.screen.blit(p1_score, (self.resolution_x/2 + self.font.size(str(self.score[0]))[0], 15))
		self.screen.blit(p2_score, (self.resolution_x/2 - self.font.size(str(self.score[1]))[0] - 14, 15))

		pygame.display.flip()

	def move_circle(self):
		self.circle_x += self.circle_speed_x * self.time_sec
		self.circle_y += self.circle_speed_y * self.time_sec

	def move_players(self):
		if self.detect_players() == 1:
			self.player_rects[0].y += self.connection.mv_p1/2
			self.move_cpu()
		else:
			self.player_rects[0].y += self.connection.mv_p1/2
			self.player_rects[1].y += self.connection.mv_p2/2

	def move_cpu(self):
		self.ia_speed = self.circle_speed * self.time_sec
		if self.circle_x >= self.resolution_x/2:
			if not self.player_rects[1].y == self.circle_y + self.circle_width:
				if self.player_rects[1].y + self.player_rects[1].height/2 < self.circle_y + self.circle_width:
					self.player_rects[1].y += self.ia_speed
				if self.player_rects[1].y > self.circle_y - self.player_rects[1].height/2:
					self.player_rects[1].y -= self.ia_speed
			else:
				self.player_rects[1].y = circle_y + circle_width	

	def collisions(self):
# Circle
		if self.circle_x <= self.player_rects[0].x + self.circle_width + 10:
			if self.circle_y >= self.player_rects[0].y and self.circle_y <= self.player_rects[0].y + self.player_rects[0].height:
				self.circle_speed_x = -self.circle_speed_x
		if self.circle_x >= self.player_rects[1].x - self.circle_width + 10:
			if self.circle_y >= self.player_rects[1].y and self.circle_y <= self.player_rects[1].y + self.player_rects[1].height:
				self.circle_speed_x = -self.circle_speed_x

		if self.circle_y <= self.circle_width + 10:
			self.circle_speed_y = -self.circle_speed_y
		if self.circle_y >= self.resolution_y - self.circle_width - 10:
			self.circle_speed_y = -self.circle_speed_y

		if self.circle_x > self.resolution_x:
			self.circle_x = self.resolution_x/2 - self.circle_width
			self.circle_y = self.resolution_y/2 - self.circle_width
			self.circle_speed_x = -self.circle_speed_x
			self.score[1] += 1
		if self.circle_x < 0:
			self.circle_x = self.resolution_x/2 - self.circle_width
			self.circle_y = self.resolution_y/2 - self.circle_width
			self.circle_speed_x = -self.circle_speed_x
			self.score[0] += 1

# Players
		for player in self.player_rects:
			if player.y <= 11.:
				player.y = 11
			if player.y >= self.resolution_y - player.height - 12.:
				player.y = self.resolution_y - player.height - 12.

	def __init__(self, screen, resolution_x, resolution_y):
# Display variables
		self.screen = screen
		self.resolution_x = resolution_x
		self.resolution_y = resolution_y

# Control
		self.time_passed = None
		self.time_sec = None

# Draw - variables
		self.white, self.red = (255, 255, 255), (255, 0, 0)
		self.score = [0, 0]
		self.font = pygame.font.Font("data/font.TTF", 30)
	# - rects
		self.bar_rects = [pygame.Rect(0, 0, self.resolution_x, 10),
						  pygame.Rect(0, self.resolution_y - 11, self.resolution_x, 11),
						  pygame.Rect(self.resolution_x/2, 0, 10, self.resolution_y)]
		self.player_rects = [pygame.Rect(10, .4*self.resolution_y, 
										 self.resolution_x/90, self.resolution_y/5),
							pygame.Rect(self.resolution_x - 25, .4*self.resolution_y, 
										 self.resolution_x/90, self.resolution_y/5)]

# Circle properties
		self.circle_width = self.resolution_x/70
		self.circle_x = self.resolution_x/2 - self.circle_width
		self.circle_y = self.resolution_y/2 - self.circle_width
		self.circle_speed_x = resolution_y/2
		self.circle_speed_y = resolution_y/2
		self.circle_speed = resolution_y/2
		self.ia_speed = 0

# Device connector
		self.connection = Device.Monitor()
		self.run()