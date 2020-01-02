#! /usr/bin/python

# Cryptomsg
# by: Darian

import string
import random
import math

#charlist = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'x', 'y', 'Y', 'z', 'Z', '.', ',', '?', '/', '\\', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '+', "'", '"', ':', ';', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

charlist = list(string.printable)
# print(len(charlist))
# print(charlist[((42+87) % len(charlist))])


def otpgen(msglen=1024, participants='DD', numOfFiles=1):
	for i in range(int(numOfFiles)):
		namedFile = open('{}{}.txt'.format(participants, random.randint(1000, 999999)), 'w+')
		for j in range(int(msglen - 1)):
			digitRep = int(random.uniform(0, len(charlist)))
			namedFile.write(str(digitRep) + ' ')
		namedFile.close()
		#print(namedFile.read())

def encrypt(plaintext=None, pad=None, ciphertext='sendMe.txt'):
	with open(plaintext , 'r+') as plainFile:
		plainFileText = plainFile.read()
	listedPlain = list(plainFileText)
	with open(pad, 'r+') as padFile:
		padFileText = padFile.read()
	listedPad = padFileText.split(' ')
	#print(len(listedPad), len(listedPlain))
	cipherFile = open(ciphertext, 'w+')
	counter = 0
	for character in range(len(listedPlain)):
		indexedChar = charlist.index(listedPlain[character])
		toWrite = str(indexedChar + int(listedPad[character]))
		cipherFile.write(toWrite + ' ')
		counter += 1
	for paddingcount in range(len(listedPad) - counter):
		cipherFile.write(str(int(random.uniform(0, 2 * len(charlist)))) + ' ')
	cipherFile.close()


if __name__ == '__main__':
	encrypt(plaintext='test.txt', pad='DD604063.txt')
	#otpgen()
