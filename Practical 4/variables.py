a = 40 
b = 36 
c = 30 
d = a-b 
e = b-c 
if d < e:
    print("e is greater and have greater improvement on running time")
else:
    print ("d is greater and have greater improvement on running time")

# and 
# F F F (T) not F = T
# F T F (T) not F = T
# T T T (F) not T = F 
X = a < b 
Y = b > c 
W = not (X and Y) 
print (X, Y, W) 
