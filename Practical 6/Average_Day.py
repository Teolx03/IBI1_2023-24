# plot a garph to describes the average day of a university student 

# import the tools to visualize 2D graph 
import matplotlib.pyplot as plt 

# create a dictionary to record data provided in practical 6 guidance 
activity_hours = {
    "Sleeping": 8,
    "Classess": 6 , 
    "Studying": 3.5, 
    "TV": 2,
    "Music" :1
 } 

# create a new entry "other" to dictionary 
Other = 24 - sum (activity_hours.values())
activity_hours["Other"] = Other

# create a variable of the requested activity ()
request_activity = "Sleeping"

# find out from the dictionary and print hours sepnd of requested activity 
activity_time = activity_hours.get (request_activity, "Error occur")
print ("Number of hours sepnd on" + str(request_activity) + "during average day: " + str(activity_time))

# print number of hours spent on the request activity during an average day 
average_time_spent = sum(activity_hours.values())/len (activity_hours)
print ("Average number of hours spent on one activity is : " + str(average_time_spent) + " hours")

# plot a pie chart based on the dictionary 
plt.figure()
plt.pie(activity_hours.values(), labels = activity_hours.keys(), startangle = 90)
plt.show()
plt.clf()
