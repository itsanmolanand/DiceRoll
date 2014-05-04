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

number_of_dice = int_input("How many dice do you want to roll? ")			
number_of_sides = int_input("How many sides are on the dice? ")

number = 0
for dice in range(1, number_of_dice + 1):
	number += random.randint(1, number_of_sides)

print "You rolled %d dice and the number was: %d" % (number_of_dice, number)



