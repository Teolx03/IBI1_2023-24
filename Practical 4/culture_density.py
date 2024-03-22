a = 5 # start from 5% density
day = 1  # in day 1 
print ("Day", str(day), ":",str(a)) 
while a <=90:   #stop while the plate cell excess 90 %
    day = day+1  #add a day once the code loop (next day)
    a = a*2      #cell double every 24 hr 
    print ("Day", str(day), ":", str(a))
print ("On day 6 the cell density goes over 90% , maiximum 5 days holiday from the lab.")

#day 6 : 160 as output because when a=80, it still can enter the loop and give an a=160 output.
#Then the a=160 cant enter the loop 
   
