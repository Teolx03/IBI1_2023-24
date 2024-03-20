# What does this piece of code do?
# Answer: Calculate a total random number after 99 times progression (<100) and get output within 99-1000

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0  # let the progress start from 0 
total_random_number=0  # let the total_random_number start from 0 
while progress<100: # the loop will run until progress variable = 99
	progress+=1     # progress variable +1 eveytime when the loop run 
	n = randint(1,10)  # a number from 2 to 10 will randomly been choosed everytime loop 
	total_random_number = total_random_number+n  # add the total random number to n everytime loop 
	
print(total_random_number)  # get output within 99-1000 

#The output will be different everytime because n is a random number

