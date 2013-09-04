#!/usr/bin python

import sqlite3

class Database:
	
	connection = sqlite3.connect('data/database.db')
	cursor = connection.cursor()

	def __init__(self):
		self.cursor.execute(
			'''CREATE TABLE scores ( 
			    id       INTEGER PRIMARY KEY ASC AUTOINCREMENT
			                     NOT NULL
			                     UNIQUE,
			    player1  TEXT    NOT NULL,
			    player2  TEXT    NOT NULL,
			    splayer1 INTEGER NOT NULL,
			    splayer2 INTEGER NOT NULL 
			);''')
		self.connection.commit()

	def save(self, s_players, n_players):
		self.cursor.execute("INSERT INTO scores VALUES (NULL, '%s', '%s', '%s', '%s');" % (
			s_players[0], s_players[1], n_players[0], n_players[1]))
		self.connection.commit()

	def seekASC(self):
		self.cursor.execute("SELECT * FROM scores ORDER BY splayer1 ASC;")
		return self.fetchall()