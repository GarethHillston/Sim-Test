import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

gridSize = 100
maxIterations = 50
numSeeds = 5
virality = 0.2

now = datetime.now().strftime("%d_%m_%y__%H%M%S")
outputFolder = "./plots/{dateTime}".format(dateTime=now)
os.mkdir(outputFolder)

# Initialise cells
locs = np.zeros((gridSize, gridSize), dtype=float)
centre = gridSize // 2
gridQuarter = gridSize // 4
for i in range(numSeeds):
    seedX = np.random.randint(centre - gridQuarter, centre + gridQuarter)
    seedY = np.random.randint(centre - gridQuarter, centre + gridQuarter)
    locs[seedX, seedY] = 1


def replot():
    figure = plt.figure()
    axes = figure.add_subplot(111)
    image = axes.pcolormesh(locs, cmap=plt.get_cmap('inferno'), vmin=0, vmax=1)
    figure.colorbar(image, ax=axes)
    plt.savefig('{outputFolder}/sim-{iter:03d}.png'.format(outputFolder=outputFolder, iter=i))
    plt.close()


replot()
for i in range(maxIterations):
    newLocs = locs.copy()

    # for each live cell, spread to neighbouring dead cells
    for x in range(gridSize):
        for y in range(gridSize):
            if locs[x, y] >= 1:
                xStart, xStop = max(x - 1, 0), min(x + 1, gridSize)
                yStart, yStop = max(y - 1, 0), min(y + 1, gridSize)
                newLocs[xStart, y] += min(newLocs[xStart, y] + virality, 1)
                newLocs[xStop, y] += min(newLocs[xStop, y] + virality, 1)
                newLocs[x, yStart] += min(newLocs[x, yStart] + virality, 1)
                newLocs[x, yStop] += min(newLocs[x, yStop] + virality, 1)
    locs = newLocs.copy()

    replot()
