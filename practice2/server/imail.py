#!/usr/bin/python3
# coding: UTF-8

import json, sqlite3

class imail:
	def __init__(self):
		return

	@staticmethod
	def load():
		conn = sqlite3.connect('emails.db')
		cursor = conn.cursor()

		# lendo os dados
		cursor.execute('SELECT * FROM emails;')

		for linha in cursor.fetchall():
			print(linha)
		conn.close()

	@staticmethod
	def new():
		conn = sqlite3.connect('emails.db')
		cursor = conn.cursor()

		cursor.execute('INSERT INTO emails ("to", "from", to_idDomain, from_idDomain)'
					   'VALUES (\'iguit0@github.com\', \'matheusrv@email.com\', 2, 1)')
		conn.commit()

		print('Dados inseridos com sucesso.')

		conn.close()

	@staticmethod
	def delete():
		conn = sqlite3.connect('clientes.db')
		cursor = conn.cursor()

		id_cliente = 8

		# excluindo um registro da tabela
		cursor.execute("""
		DELETE FROM emails
		WHERE id = ?
		""", (id_cliente,))

		conn.commit()

		print('Registro excluido com sucesso.')

		conn.close()
