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
from math import sqrt
from serial import SerialException
import serial.tools.list_ports as list_ports

import threading
from threading import Thread

class Monitor(Thread):

	def __init__(self):
		self.event = threading.Event()
		self.connection = serial.Serial()
		self.players = 0
		self.mv_p1 = 0
		self.mv_p2 = 0

	def start(self):
		Thread.__init__(self)
		Thread.start(self)

	def stop(self):
		self.event.set()
		self._Thread__stop()

	def run(self):
		for rootPort in list_ports.comports():
			for port in rootPort:
				if 'ttyUSB' in port:
					self.connection.port = port
					self.connection.baudrate = 9600
					try:
						self.connection.open()
					except SerialException, ex:
						print "Unable to connect the device \n%s" % str(ex)
						self.event.set()
		while self.isAlive and self.connection.isOpen():
			try:
				line = self.connection.readline()
				self.players, x, y, z = int(line.split(" ")[0]), int(line.split(" ")[1]), int(line.split(" ")[2]), int(line.split(" ")[3])
				mv_y = sqrt(x**2 + y**2 + z**2)
				if self.players == 1:
					if mv_y <= 115 and mv_y >= 85:
						self.mv_p1 = 0
					else:
						if mv_y <= 100:
							self.mv_p1 = mv_y
						else:
							self.mv_p1 = -mv_y/2.5
				else:
					if mv_y <= 115 and mv_y >= 85:
						self.mv_p2 = 0
					else:
						if mv_y <= 100:
							self.mv_p2 = -mv_y
						else:
							self.mv_p2 = mv_y/2.5

			except Exception, ex: 
				print "%s" % ex