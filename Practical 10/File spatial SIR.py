import numpy as np 
import matplotlib.pyplot as plt 

population = np.zeros((100,100))
outbreak = np.random.choice (range(100),2)
population [outbreak[0], outbreak[1]] = 1

plt.figure(figsize = (6,4), dpi = 150)
plt.imshow(population, cmap = "viridis", interpolation = "nearest")
plt.show()
plt.clf()

beta = 1/8
gamma = 0.1

# infect each neighbour with probability beta
# infect all 8 neighbours (this is a bit finicky, is there a better way?):
def infected_neighbors (a,b):
    for x in range(a-1,a+2):
        for y in range(b-1,b+2):
            # don't infect yourself! (Is this strictly necessary?)
            if (x,y) != (a,b):
                # make sure I don't fall off an edge
                if x != -1 and y != -1 and x!=100 and y!=100:
                    # only infect neighbours that are not already infected!
                    if population[x,y]==0:
                        population[x,y]=np.random.choice(range(2),1,p=[1-beta,beta])[0]

for l in range (100):
    infected_point = np.where(population ==1)
    for a,b in zip(infected_point[0], infected_point[1]):
        infected_neighbors (30,70)
        if np.random.rand() < gamma:
            population [50,50] = 2

# plot the graph 
plt.figure (figsize=(8,6))
plt.imshow(population, cmap ="viridis", interpolation = "nearest")
plt.colorbar (label="state (0:susceptible, 1: Infected, 2: Recovered)")
plt.title ("Spatial SIR")
plt.xlabel ("x-coordinate")
plt.ylabel ('y-coordinate')
plt.show()




# find infected points
infectedIndex = np.where(population==1)
# loop through all infected points
for i in range(len(infectedIndex[0])):
    # get x, y coordinates for each point
    x = infectedIndex[0][i]
    y = infectedIndex[1][i]
                           