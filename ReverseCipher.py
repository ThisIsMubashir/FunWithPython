#!/usr/bin/env python


def main():

	msg = raw_input("Please Enter the message: ")
	cipherMsg = ''
	lenMsg = len(msg)

	while lenMsg != 0 :
		cipherMsg += msg[lenMsg-1]
		lenMsg = lenMsg-1

	print "Your Cipher text is : ",cipherMsg 


if __name__ == '__main__':
	main()