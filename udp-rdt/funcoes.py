#!/usr/bin/env python3
"""
                UDP-RDT
https://github.com/iguit0/Redes-De-Computadores
"""

__author__ = "Igor Alves"
__version__ = "0.0.1"
__license__ = "GPL-3.0"

import sys

def menu(vetor):
	#os.system('clear')
	print("\n----------------------------------------------")
	print("Lista de pacotes a serem enviados: ")
	print(vetor[0:len(vetor)-1])
	print("\nOpções:")
	print("\n1 - Enviar próximo pacote")
	print("2 - Corromper envio do próximo pacote")
	print("3 - Duplicar envio do próximo pacote")
	print("4 - Embaralhar pacotes")
	print("5 - Sair\n")
	escolha = 0
	while (escolha<1 or escolha>5):
		escolha = int(input("Opção escolhida: "))
	return escolha

#Calcula complemento de 1
def complemento(n, tamanho):
    comp = n ^ ((1 << tamanho) - 1)
    return '0b{0:0{1}b}'.format(comp, tamanho)

#Soma de verificação
def checksum(portaorigem,portadestino,comprimento):
	primeirasoma = bin(portaorigem+portadestino)[2:].zfill(16)
	if (len(primeirasoma)>16):
		primeirasoma = primeirasoma[1:17]
		primeirasoma = bin(int(primeirasoma,2) + 1)[2:].zfill(16)
	segundasoma = bin(int(primeirasoma,2)+comprimento)[2:].zfill(16)
	if (len(segundasoma)>16):
		segundasoma = segundasoma[1:17]
		segundasoma = bin(int(segundasoma,2) + 1)[2:].zfill(16)
	checksum = complemento(int(segundasoma,2),16)[2:]
	return int(checksum,2)