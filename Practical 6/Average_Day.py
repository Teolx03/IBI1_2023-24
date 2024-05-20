# plot a garph to describes the average day of a university student 

# import the tools to visualize 2D graph 
import matplotlib.pyplot as plt 

activity_hours = {
    "Sleeping": 8,
    "Classess": 6 , 
    "Studying": 3.5, 
    "TV": 2,
    "Music" :1
 } 
 
Other = 24 - sum (activity_hours.values())
activity_hours["Other"] = Other

request_activity = "Sleeping"

activity_time = activity_hours.get (request_activity, "Error occur")
print ("Number of hours sepnd on" + str(request_activity) + "during average day: " + str(activity_time))

average_time_spent = sum(activity_hours.values())/len (activity_hours)
print ("Average number of hours spent on one activity is : " + str(average_time_spent) + " hours")

# plot for a pie chart 
plt.figure()
plt.pie(activity_hours.values(), labels = activity_hours.keys(), startangle = 90)
plt.show()
plt.clf()
