import numpy as np
from datetime import datetime
import os
import plotting
import spreadmodels

gridSize = 100
maxIterations = 50
numSeeds = 5
shading = 'flat'
infectiousThreshold = 0.2
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

for i in range(maxIterations):
    plotting.replot(shading, outputFolder, i, locs)
    locs = spreadmodels.spread_basic_threshold(locs, gridSize, infectiousThreshold, virality)

plotting.replot(shading, outputFolder, maxIterations + 1, locs)
