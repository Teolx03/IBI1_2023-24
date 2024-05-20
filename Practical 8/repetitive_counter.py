# write a code to indentify gene which contain repetitive element 

# import necessary tools 
import re

# import sequence provided in practical 8 guidance 
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'

# initialize a counter 
count = 0 

# check for the repetitive sequence pattern 
if re.findall(r"GTCTGT",seq):
    count = count+1
if re.findall(r"GTGTGT",seq):
    count = count+1

print ("Repetitive count: " + str(count))


    