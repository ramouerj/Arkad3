#!/usr/bin python

'''
ST   ----> I/O 12
GSEL ----> I/O PWM 10
0 GD ----> I/O PWM 11
SLP  ----> I/O 13
XOUT ----> I/O ANALOG IN 2
YOUT ----> I/O ANALOG IN 1
ZOUT ----> I/O ANALOG IN 0
GND  ----> I/O POWER GND
VCC  ----> I/O 3V3
'''

import serial
import time
from serial import SerialException
import serial.tools.list_ports as list_ports

import threading
from threading import Thread

event = threading.Event()
event_player_1 = threading.Event()
event_player_2 = threading.Event()

class CPU(Thread):

	def __init__(self):
		super(CPU, self).__init__()

	def run(self):
		while True:
			pass
			# Fazer o CPU

class Player(Thread):
	def __init__(self, name):
		super(Player, self).__init__()
		self.name = name
		self.connection = serial.Serial()
		self.connected = list()
		self.mv_p1, self.mv_p2 = 0, 0
		self.player1_isAlive, self.p2_isAlive = True, True

	def start(self):
		Thread.start(self)

	def run(self):
		global event, event_player1, event_player2

		for rootPort in list_ports.comports():
			for port in rootPort:
				if 'ttyUSB' in port and not port in self.connected:
					self.connection.port = port
					self.connection.baudrate = 9600
					try:
						self.connection.open()
						self.connected.append(port)
					except SerialException, ex:
						print "Could not open connection.\n %s" % str(ex)
						event.set()
		# Verificar o número de jogadores
		while True:
			if not self.p1_isAlive:
				event.set()
				event_player1.wait()
			if not self.p2_isAlive:
				event.set()
				event_player2.wait()


class Monitor(Thread):

	def __init__(self):
		self.threads = list()

	def start(self):
		Thread.__init__(self)
		Thread.start(self)

	def run(self):
		th_p1 = Player('player_1')
		th_p2 = Player('player_2')

		while True:
			global event
			if th_p1.