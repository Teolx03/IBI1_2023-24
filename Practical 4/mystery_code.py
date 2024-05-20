# What does this piece of code do?
# Answer:This code run 100 times and generate a sum of 100 random numbers between 1 and 10 

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# initialise the variable 
progress=0  # let the progress start from 0 
total_random_number=0  # let the total_random_number start from 0 

while progress < 100: # the loop will run until progress variable = 99 (code run 100 time)
	progress+=1     # progress variable +1 eveytime when the loop run 
	n = randint(1,10)  # a number between 1 and 10 will randomly been choosed everytime loop 
	total_random_number = total_random_number+n  # add the total random number to n everytime loop 
	
print(total_random_number)  # sum of 100 random numbers between 1 and 10

#The output will be different everytime because n is a random number