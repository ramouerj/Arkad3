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

import time
import threading
from threading import Thread

import serial
import serial.tools.list_ports as list_ports
from serial import SerialException

class Sync(Thread):
	def __init__(self):
		pass

class Update(Thread):
	
	connected = []
	connection = serial.Serial()
	isAlive = True
	coordinates = [0, 0]

	def __init__(self, name):
		Thread.__init__(self, name = name)
		self.interval = 0
		self.finished = threading.Event()
		for rootPort in list_ports.comports():
			for port in rootPort:
				if 'ttyUSB' in port and not port in self.connected:
					self.connection.port = port
					self.connection.baudrate = 9600
					try:
						self.connection.open()
					except SerialException, ex:
						print "Could not open connection.\n%s" % str(ex)
						exit()

	def start(self):
		Thread.__init__(self)
		Thread.start(self)

	def stop(self):
		self.finished.set()
		self._Thread__stop()

	def run(self):
		while self.isAlive and self.connection.isOpen():
			try:
				list = self.connection.readline().split(" ")
				list[1] = list[1].replace("\n", "").replace("\r", "")
				self.coordinates = (int(list[0]), int(list[1]))
			except:
				pass
		self.stop()
