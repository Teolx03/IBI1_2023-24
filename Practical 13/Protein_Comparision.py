# Open all the fasta files and read it 
read_seq1 = open ('C:\\Users\\lixia\\IBI1_2023-24\\IBI1_2023-24\\Practical 13\\SLC6A4_HUMAN.fa', "r")
read_seq2 = open ('C:\\Users\\lixia\\IBI1_2023-24\\IBI1_2023-24\\Practical 13\\SLC6A4_MOUSE.fa', "r")
read_seq3 = open ('C:\\Users\\lixia\\IBI1_2023-24\\IBI1_2023-24\\Practical 13\\SLC6A4_RAT.fa', "r")

# Define a function to extract the amino acid sequences only 
def target_sequence (sequence):
    seq = ""
    for line in sequence:
        if line.startswith('>'):
          continue
        else:
          seq += line.strip()
    return (seq)

# Extract the amino acid sequences for the 3 files 
human_seq = target_sequence(read_seq1)
mouse_seq = target_sequence (read_seq2)
rat_seq = target_sequence (read_seq3)

# Calculate and print the percentage of identical amino acids for human and mouse     
distance = 0 
for i in range (len(human_seq)):
   if human_seq [i] != mouse_seq [i]:
      distance += 1 
print ("Number of difference amino acids between human and mouse is " + str(distance))
identical_human_and_mouse = ((len(human_seq) - distance) / len(human_seq))*100
print ("Percentage identical amino acids for human and mouse is " + str(identical_human_and_mouse) + "%")

# Calculate and print the percentage of identical amino acids for human and rat
distance = 0
for i in range (len(human_seq)):
   if human_seq [i] != rat_seq[i]:
      distance += 1 
print ("Number of different amino acids between human and rat is " + str(distance))
identical_human_and_rat = ((len(human_seq) - distance) / len(human_seq)) * 100 
print ("Percentage identical amino acids for human and rat is " + str(identical_human_and_rat) + "%")

# Caluclate and print the percentage of identical amino acids for mouse and rat 
distance = 0 
for i in range (len(mouse_seq)):
   if mouse_seq [i] != rat_seq[i]:
      distance += 1
print ("Number of different amino acids for mouse and rat is " + str(distance))
identical_mouse_and_rat = ((len(mouse_seq) - distance) / len(mouse_seq)) * 100 
print ("Percentage identical amino acids for mouse and rat is " + str(identical_mouse_and_rat) + "%")

# Import nessaccary tool to find the alignment of amino aicds 
import blosum as bl 
matrix = bl.BLOSUM(62)

# Calculate and print the alignment score for human and mouse amino acids 
alignment_score = 0
for l in range (len(human_seq)):
   aa_human = human_seq [l]
   aa_mouse = mouse_seq [l]
   alignment = matrix[aa_human][aa_mouse]
   alignment_score += alignment
print ("Alignment score for human and mouse amino acids " + str (alignment_score))

# Calculate and print the alignment score for human and rat amino acids 
alignment_score = 0
for l in range (len(human_seq)):
   aa_human = human_seq [l]
   aa_rat = rat_seq [l]
   alignment = matrix[aa_human][aa_rat]
   alignment_score += alignment
print ("Alignment score for human and rat amino acids " + str (alignment_score))

# Calculate and print the alignment score for mouse and rat amino acids 
alignment_score = 0
for l in range (len(rat_seq)):
   aa_rat = rat_seq [l]
   aa_mouse = mouse_seq [l]
   alignment = matrix[aa_rat][aa_mouse]
   alignment_score += alignment
print ("Alignment score for mouse and rat amino acids " + str (alignment_score))


