# find out each person's favourite James Bond actor by using the theory 
# Theory: each person's favourite James Bond is the person who played the character when they turn 18 

# define a fucntion to find out an individual's favourite James Bond 
def favourite_character (born_year):
   # a dictionary about the actors portrayed James Bond in different years
   James_Bond_actor = {'Roger Moore' : (1973,1986),
      'Timothy Dalton' : (1987, 1994),
      'Pierce Brosnan' : (1995,2005),
      'Daniel Craig' : (2006,2021)
    }
   
   # calculate the year when a person turn 18 
   Year_Turn_18 = born_year + 18

   # loop with the "James_Bond_actor" dictionary
   for actor, (year_start, year_end) in James_Bond_actor.items():
      # check if when the year of perosn trun 18 fall in the range of year the actor portrayed James Bond
      if Year_Turn_18 >= int(year_start) and Year_Turn_18<= int(year_end):
       return (actor)
   return ("Error")

# Call out the fucntion with specific born_year 
print ("Favourite character is", favourite_character(born_year=1980))



