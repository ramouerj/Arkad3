#!/usr/bin python

import time
import threading
from threading import Thread

import serial
import serial.tools.list_ports as list_ports
from serial import SerialException

class Update(Thread):
	
	connection = serial.Serial()
	isAlive = True
	coordinates = [0, 0]

	def __init__(self):
		Thread.__init__(self)
		self.interval = 0
		self.finished = threading.Event()
		for rootPort in list_ports.comports():
			for port in rootPort:
				if 'ttyUSB' in port:
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
		while self.isAlive:
			try:
				list = self.connection.readline().split(" ")
				list[1] = list[1].replace("\n", "").replace("\r", "")
				self.coordinates = (int(list[0]), int(list[1]))
			except:
				pass
		self.stop()
