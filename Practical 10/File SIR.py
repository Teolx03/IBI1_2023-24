# import necessary tools 
import numpy as np 
import matplotlib.pyplot as plt 

# Initialise the variables according to the practical guidance 
Population = 10000
Infected = 1 
Suspected = Population - Infected 
Recovered = 0
beta = 0.3   # infection probability 
gamma = 0.05  # recovery probability 

# create array to track how variables change over time 
S = [Suspected]
I = [Infected]
R = [Recovered]

# loop over 1000 timepoint 
for time in range (1000):
    Infected_probability = beta * I[-1] / Population 
    Recovered_probability = gamma 
    
    # using random.choice function to generate new infected and recovary cases
    new_infected = np.random.choice([0,1],S[-1],[1-Infected_probability, Infected_probability])
    new_recovery = np.random.choice([0,1], I[-1],[1-Recovered_probability, Recovered_probability])

    # update all the array with the generated new case 
    S.append (S[-1] - np.sum(new_infected))
    I.append (I[-1] + np.sum(new_infected) - np.sum(new_recovery))
    R.append (R[-1] + np.sum(new_recovery))


# plot a SIR model with vaccination rate graph 
plt.figure(figsize= (12,6))
plt.plot (S, label = "Susceptible")
plt.plot (I, label = "Infected")
plt.plot (R, label = "Recovered")
plt.title ("SIR model")
plt.xlabel ("Number of people")
plt.ylabel ("Time")
plt.legend() # for figure legend 
plt.show()
plt.clf()