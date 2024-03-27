# create 2 different bar graph in one figure 

import matplotlib.pyplot as plt # import matplotlib to visualize 2D graph 

# BAR GRAPH 1 
UK_cities_lable = ["Edinburgh", "Glasgow", "Stirling", "London"]  # name for each bar 
uk_cities = [0.56, 0.62, 0.04, 9.7] # height for each bar
width = 0.5 # bar width 

plt.figure() # plot the figure 
plt.subplot(2,1,1) #create a first subplot in 2x1 grid and the last "1" means 1st graph
plt.bar (UK_cities_lable, uk_cities, width ) #plot a bar graph, 1st = bar name(x-axis), 2nd = height(y-axis), 3rd = bar width)
plt.ylabel ("Population") # label the y-axis 
plt.title ("Population in UK") # title of graph 

# BAR GRAPH 2
China_cities_label = ["Haining", "Hangzhou", "Shanghai", "Beijing"] 
china_cities = [0.58, 8.4, 29.9, 22.2]
width = 0.5 

plt.subplot(2,1,2) # graph 2 
plt.bar (China_cities_label, china_cities, width)
plt.ylabel ("Population")
plt.title ("Population in China")

plt.tight_layout() # Adjust layout prevent overlap 
plt.show() # Show the graph 
plt.clf() # clear the graph 

