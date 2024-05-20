# import necessary libraries 
import numpy as np 
import matplotlib.pyplot as plt 

# Initialise the variables according to the practical guidance
Population = 1000 
Infected = 1 
Suspected = Population - Infected 
Vaccination_rate = 0.3
Vaccinated = Population * Vaccination_rate
Recovered = 0
beta = 0.3
gamma = 0.05

# create array to track how variables change over time 
S = [Suspected]
I = [Infected]
R = [Recovered]
V = [Vaccinated]

# loop over 1000 timepoint 
for time in range (1000):
    Infected_probability = beta * I[-1] + V[-1] / Population 
    Recovered_probability = gamma 
    
    # using random.choice function to generate new infected and recovary cases
    new_infected = np.random.choice([0,1],S[-1],[1-Infected_probability, Infected_probability])
    new_recovery = np.random.choice([0,1], I[-1],[1-Recovered_probability, Recovered_probability])

    # update all the array with the generated new case 
    S.append (S[-1] - np.sum(new_infected))
    I.append (I[-1] + np.sum(new_infected) - np.sum(new_recovery))
    R.append (R[-1] + np.sum(new_recovery))
    V.append (V[-1])


# plot a graph for the data 
plt.figure(figsize= (12,6))
plt.plot (I, label = "30%")
plt.title ("SIR model with vaccination rate")
plt.xlabel ("Number of people")
plt.ylabel ("Time")
plt.legend()
plt.show()
plt.clf()