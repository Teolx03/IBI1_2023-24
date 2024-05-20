# learn to analyse a public health dataset in python 

# import the necessary tools 
import os 
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

# make sure the working directory 
os.chdir("C:\\Users\\lixia\\IBI1_2023-24\\IBI1_2023-24\\Practical 7")
# os.listdir()
# os.getcwd()

# read the dataset into a pandas DataFrame 
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#print (dalys_data.head(5)) # see the first 5 data in data frame 
#print (dalys_data.info())  # what type of the data eg. how many rows, columns)
#print (dalys_data.describe()) # Calculate each mean, range, standard deviation.. 

# using iloc access specific value by row num and colum num [row,column]
#print (dalys_data.iloc[0,3]) # 1st row, 2nd column 
#print (dalys_data.iloc[2,0:5]) # 3rd row, 1-4column 
#print (dalys_data.iloc[0:2,:]) # first 2 row, all column 
#print (dalys_data.iloc[0:10:2,0:5]) # first 10 rows, 2 = select every 2nd row from index 0, first 4  column)
print (dalys_data.iloc[0:101:10,3]) # first 100 rows(include 100), every 10th row, fourth column 

# Use Boolean to access entries
#print (dalys_data.iloc[0:3,[0,1,3]]) #first 3 row, first, second, fourth column 
#my_columns = [True, True, False, True] 
#print (dalys_data.iloc[0:3,my_columns]) # Python will only read the column with "True"
#columns = [True, True, True, True]
#print (dalys_data.iloc[0:30,columns]) 

# Using loc (name)
#print (dalys_data.loc[2:4,"Year"]) # row num 2 to 4, year column 
#print (dalys_data.loc[0:29,"DALYs"])
#print (dalys_data.loc[0: , "Entity"]) #all row, entity column 
print (dalys_data.loc[dalys_data["Entity"] == "Afghanistan", "DALYs"])

# extract data for China
china_column = [True, False, True, True ]
china_data = dalys_data.loc[dalys_data["Entity"] == "China", china_column]
print (china_data)
china_DALYs = china_data.loc[0: , "DALYs"]
china_mean = np.mean(china_DALYs)
print ("China total mean DALYs: " + str(china_mean))
if china_mean > (dalys_data.iloc[1169, 3]):
    print ("2019 was below the mean" )
china_year = china_data.loc [0: , "Year"]

# plot a graph for China data 
plt.figure()
plt.plot(china_year, china_DALYs, "b+") # b+ = plot data using + sign and in blue color 
plt.xticks(china_year, rotation = -90) # plot all x-axis variables
plt.title ("DALYs over time in China")
plt.grid(True)
plt.show()
plt.clf()


# FOR File question.txt 
# extract data for United Kingdom 
UkData = dalys_data.loc [dalys_data["Entity"] == "United Kingdom"] 
UkYear = UkData["Year"]
UkDALYs = UkData ["DALYs"]

# plot a graph for DALYS changed in UK over time 
plt.figure()
plt.plot (UkYear, UkDALYs, "b+")
plt.title ("DALYs changed in UK over time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.grid(True)
plt.show()
plt.clf()


