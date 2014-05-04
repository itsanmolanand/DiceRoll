#!/usr/bin/wpython
import random 

def int_input(sentence):
	while True:
		number = raw_input(sentence)
		try:
			number = int(number)
			if number <= 0:
				print "Please enter a number greater than zero"
			else:	
				return number
		except:
			print "Not a number"
			
side = int_input("How many sides are on the dice? ")
number = random.randint(1, side) 
print "Here is the number the dice gave: %d" % (number)


