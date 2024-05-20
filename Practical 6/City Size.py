# create 2 different bar graph in one figure 

# import matplotlib to visualize 2D graph 
import matplotlib.pyplot as plt  

# BAR GRAPH 1 
# import data for first bar graph 
UK_cities_lable = ["Edinburgh", "Glasgow", "Stirling", "London"]  
uk_cities = [0.56, 0.62, 0.04, 9.7]
sorted_uk_city =  sorted (uk_cities)
print ("UK cities size : " + str(sorted_uk_city))
width = 0.5 

# plot first bar graph 
plt.subplot(2,1,1) #create a first subplot in 2x1 grid and the last "1" means 1st graph
plt.bar (UK_cities_lable, uk_cities, width ) #plot a bar graph, 1st = bar name(x-axis), 2nd = height(y-axis), 3rd = bar width)
plt.ylabel ("Population") # label the y-axis 
plt.title ("Population in UK") # title of graph 


# BAR GRAPH 2
# import data for second bar graph 
China_cities_label = ["Haining", "Hangzhou", "Shanghai", "Beijing"] 
china_cities = [0.58, 8.4, 29.9, 22.2]
sorted_china_cities = sorted (china_cities)
print ("China cities size :" + str(sorted_china_cities))
width = 0.5 

# plot the second bar graph 
plt.subplot(2,1,2) 
plt.bar (China_cities_label, china_cities, width)
plt.ylabel ("Population")
plt.title ("Population in China")

# let 2 different bar graph locate in one figure 
plt.tight_layout() # Adjust layout prevent overlap 
plt.show() 
plt.clf() 

