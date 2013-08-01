#!usr/bin python
#-*- coding:utf-8 -*-

import sqlite3

class Score :

	conexao = sqlite3.connect("data/score.db")
	cursor = conexao.cursor()

	def salvar(self, nome, score):
		self.cursor.execute("INSERT INTO score VALUES (NULL, '%s', '%d');" % (nome, score))
		self.conexao.commit()

	def deletar(self, id):
		self.cursor.execute('DELETE FROM score WHERE id = %d;' % (id))
		self.conexao.commit()

	def buscar(self):
		self.cursor.execute('SELECT * FROM score ORDER BY pontuacao ASC;')
		return self.cursor.fetchall()

	def __init__(self):
		self.cursor.execute('''CREATE TABLE IF NOT EXISTS score (
		    id    INTEGER PRIMARY KEY ASC AUTOINCREMENT
                  NOT NULL
                  UNIQUE,
    		nome  TEXT,
    		pontuacao INTEGER);''')
		self.conexao.commit()
