# The athlete are training in different method to improve time taken to complete 5km run
# Time taken for the athlete store in different variable 
# Calculate which method is more effective 

a = 40 
b = 36 
c = 30 
d = a-b 
e = b-c 
if d < e:
    print("e is greater and have greater improvement on running time")
else:
    print ("d is greater and have greater improvement on running time")

# create Boolean variable 
X = a > b   # True
Y = b < c   # False 
W = (X or Y) and not (X and Y)
print (X, Y, W) 

# Truth table for W 
# X     | Y     | W     
# -----------------------
# True  | False | True 
# False | True  | True 
# True  | True  | False 
# False | False | False 