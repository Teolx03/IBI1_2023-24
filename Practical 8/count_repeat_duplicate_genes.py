# Count the number of reprtitive sequence ("GTGTGT" or "GTCTGT") within duplicated gene and output in a new fasta file 

# import necessary tool 
import re 

# open and read a fasta file 
readfile = open('C:\\Users\\lixia\\IBI1_2023-24\\IBI1_2023-24\\Practical 8\\duplicate_genes.fa', "r")

# ask for user input 
print ("Enter the repetitive sequence, GTGTGT or GTCTGT")
repetitive_sequence = input()

# initialise the variables 
sequence = ""
gene_name = ""
repeated_GT_sequence = "GTGTGT"
repeated_CT_sequence = "GTCTGT"
count = 0 

# FOR GTGTGT REPETITIVE 
# check if user enter "GTGTGT"
if repetitive_sequence == "GTGTGT":
  
  # open a new fasta file store "GTGTGT" gene  
  newGTfile = open ("C:\\Users\\lixia\\IBI1_2023-24\\IBI1_2023-24\\Practical 8\\GTGTGT_duplicate_genes.fa", 'w')
  
  # loop over each line in the input fasta file 
  for line in readfile:
      if line.startswith ("gene"):
          count = sequence.count (repeated_GT_sequence) # count occurrence of repetitive sequences in the sequence 
          
          # input the gene name, count and sequence to the new fasta file 
          if count > 0 :
              newGTfile.write (gene_name.strip())
              newGTfile.write ('\n')
              newGTfile.write ("count:" + str(count))
              newGTfile.write ('\n')
              newGTfile.write (sequence)
              newGTfile.write ('\n')
         
          # reset the variables 
          gene_name = ""    
          gene_name += line # extract gene name
          sequence = ""
          count = 0
      else:
           # accumulate sequence to line variable 
           sequence += line 

# to print out the last sequence in input fasta file (if is contain target repetitive sequence)
  if len (sequence) > 0 and gene_name != "":
             newGTfile.write (gene_name)
             newGTfile.write (sequence)
      
# FOR GTCTGT REPETITIVE 
# check if user enter "GTCTGT"
if repetitive_sequence == "GTCTGT":
  
  # open a new fasta file store "GTGTGT" gene  
  newGTfile = open ("C:\\Users\\lixia\\IBI1_2023-24\\IBI1_2023-24\\Practical 8\\GTCTGT_duplicate_genes.fa", 'w')
  
  # loop over each line in the input fasta file
  for line in readfile:
      if line.startswith ("gene"):
          count = sequence.count (repeated_CT_sequence) # count occurrence of repetitive sequences in the sequence 
        
        # input the gene name, count and sequence to the new fasta file 
          if count > 0 :
              newGTfile.write (gene_name.strip())
              newGTfile.write ('\n')
              newGTfile.write ("count" + str(count))
              newGTfile.write ('\n')
              newGTfile.write (sequence)
              newGTfile.write ('\n')
          
          # reset the variables
          gene_name = ""    
          gene_name += line  # extract gene name
          sequence = ""
          count = 0
      else:
           # accumulate sequence to line variable
           sequence += line

  # to print out the last sequence in input fasta file (if is contain target repetitive sequence)
  if len (sequence) > 0 and gene_name != "":
             newGTfile.write (gene_name)
             newGTfile.write (sequence)

    
      
    

