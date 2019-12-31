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
		for j in range(int(msglen)):
			digitRep = int(random.uniform(0, len(charlist)))
			namedFile.write(str(digitRep) + ' ')
		namedFile.close()
		#print(namedFile.read())

def encrypt(plaintext=None, ciphertext='sendMe.txt', pad=None):
	plainFile      = open(plaintext, 'r')
	plainFileList  = list(str(plainFile.read()))
	cipherFile     = open(ciphertext, 'w+')
	cipherFileList = list(str(cipherFile.read()))
	padFile        = open(pad, 'r')
	padFileList    = str(padFile.read()).split(' ')
	counter        = 0
	charsToFile    = 0
	for character in plainFileList:
		for index in range(len(charlist)):
			if character == charlist[index]:
				#print(padFileList[counter])
				cipherFile.write(str((int(padFileList[counter]) + index) % len(charlist)) + ' ')
				charsToFile += 1
			else:
				continue
		counter += 1
	
#	print(charsToFile)
	print(len(padFileList) - charsToFile)		
	for filler in range(len(padFileList) - charsToFile):
		cipherFile.write(str(int(random.uniform(0, len(charlist)))) + ' ')
	
	cipherFile.close()
	
	cipherFile2    = open(ciphertext, 'r')
	cipherFileList2= list(str(cipherFile2.read()))
		
	for i in range(len(padFileList)):
		print((list(str(cipherFile.read()))[i + 1] + padFileList[i]) % len(charlist))
#		print(len(padFileList))
#		print(len(cipherFileList2))
		pass

	plainFile.close()
	cipherFile.close()
	padFile.close()
				
	

if __name__ == '__main__':
	#otpgen()
	encrypt(plaintext='test.txt', pad='DD531938.txt')
	#print(charlist)
