# extract all the gene whose sequence description contains the word "duplication", simplify the sequence name by only putting the gene name and output the result to a new fasta file. 

# import necessary tools 
import re 

# open and read the file 
readfile = open ('C:\\Users\\lixia\\IBI1_2023-24\\IBI1_2023-24\\Practical 8\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', "r")

# output the result in a new file 
newfile = open ('C:\\Users\\lixia\\IBI1_2023-24\\IBI1_2023-24\\Practical 8\\duplicate_genes.fa', "w")

# Initialise the variable and boolean 
sequence = ""  
gene_name = ""  
isTargetGene = False  

# loop over each line in the fasta file 
for line in readfile : 
    if line.startswith (">"):    
        if len(sequence) > 0:   
           if isTargetGene:
            newfile.write (sequence)  # input sequence to new output file 
       
        # reset for next loop
        isTargetGene = False  
        sequence = ""        
        
        # check the if the line contain keyword "duplicate"
        if 'duplication' in line:
          gene_name = re.search(r'(gene):(\S+)', line) # find the gene name in file
          newfile.write (gene_name.group())
          newfile.write ('\n')
          isTargetGene = True                     
    else:
        # accumulate the target DNA sequence 
        sequence += line  

# to print out the last sequence in file (if is target gene)
if len(sequence) > 0: 
   if isTargetGene:
    newfile.write (sequence)
