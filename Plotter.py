import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # Creates a 3d set of axis (I don't know how to write plural axis help)
dotSize = 0.5 # size of the dots on the graph, can be changed to make the dots smaller or larger


data = np.load("Bodies.npy", allow_pickle=True) # loads in the data from Simulation.py
useableData = {"y": [[], [], []], "c": [[], [], []], "m": [[], [], []], "g": [[], [], []], "r": [[], [], []]}# the sun is yellow, mercury is cyan, venus is magenta, earth is green, mars is red
for pNum in range(len(data)): # goes through numbers in range of the length of the dataset
    p = data[pNum][1] # selects an entry one after an another and ignores the time (The time is at pos 0)
    pos = getattr(p, "position") # Takes the position attribute
    c = -1
    for colorName in useableData:
        c += 1
        if c == pNum % 5: # c goes from 0 to 4. pNum is used to find which body the position belongs to.
            for cordNum in range(3):# iterates through 0,1,2 to add a position to the x list, the y list, then the z list
                useableData[colorName][cordNum].append(pos[cordNum]) # Appends each coordinate to it's own list. All of these lists is contained in a dictionary entry belogning to it's particular body.


for colorName in useableData: # Loops through each body
    xCoords = np.array(useableData[colorName][0]) # Turns each list into a numpy array
    yCoords = np.array(useableData[colorName][1])
    zCoords = np.array(useableData[colorName][2])
    ax.scatter(xCoords, yCoords, zCoords, s=dotSize, zdir='z', c=colorName, depthshade=True) # Makes a scatter plot of that planets movements

plt.xlabel("X label") # Setting the axis labels
plt.ylabel("Y label")
ax.set_zlabel('Z Label')

plt.show() # Shows all the scatter plots
print("Finished!")