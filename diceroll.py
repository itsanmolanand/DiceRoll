#!/usr/bin/wpython
import random 

def int_input(sentence, min_value):
	while True:
		number = raw_input(sentence)
		try:
			number = int(number)
			if number <= min_value:
				print "Please enter a number greater than %d" % min_value
			else:	
				return number
		except:
			print "Not a number"

number_of_dice = int_input("How many dice do you want to roll? ", 0)			
#number_of_sides = int_input("How many sides are on the dice? ", 1)

number = 0
for dice in range(1, number_of_dice + 1):
	# get the number of sides here instead
	number += random.randint(1, number_of_sides)

print "You rolled %d dice and the number was: %d" % (number_of_dice, number)



