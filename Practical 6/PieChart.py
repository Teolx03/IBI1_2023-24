
import matplotlib.pyplot as plt #import the tools to visualize 2D graph 

activity = ["Sleeping", "Classess", "Studying", "TV", "Music","Other"]
timespent = [8, 6, 3.5, 2, 1,3.5]
plt.figure()
plt.pie(timespent, labels = activity, startangle = 90)
plt.show()
plt.clf()
