import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

gridSize = 50
maxIterations = 10
numParticles = 100

now = datetime.now().strftime("%d_%m_%y__%H%M%S")
outputFolder = "./plots/{dateTime}".format(dateTime=now)
os.mkdir(outputFolder)

fig = plt.figure()
ax = fig.add_subplot(111)

# colour map
colours = np.random.randint(0, numParticles, size=(numParticles))

# Initialise all particles to the centre
locations = np.ones((numParticles, 2), dtype=int) * gridSize//2

for i in range(maxIterations):
    # randomly move particles
    locations += np.random.randint(-1, 2, locations.shape)

    for j in range(numParticles):
        x, y = locations[j]

    print(i + 1, '/', maxIterations)

    transLocs = locations.transpose()

    # clear previous plot and replot
    ax.clear()
    ax.scatter(transLocs[0], transLocs[1], c=colours, alpha=0.5)

    plt.savefig('{outputFolder}/sim-{iter:03d}.png'.format(outputFolder=outputFolder, iter=i))
    # plt.show()
