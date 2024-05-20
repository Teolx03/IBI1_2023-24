# determine how many chocolate bars the user is able to afford at the supermarket 

# define a fucntion with 2 parameters 
def chocolate_bars(total_money, price):
    # calculate the total number of chocalate can be bought and the remaining money 
    number_of_bar = total_money / price
    total_number_of_bar = int(number_of_bar)
    money_return = total_money - (total_number_of_bar*price) 
    print ("Number of bars that can be bought: " + str (total_number_of_bar))
    print ("Money return: " + str (money_return))
    
# call out the function with example arguments 
example = (chocolate_bars(100,8))
