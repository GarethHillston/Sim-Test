import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

gridSize = 50
maxIterations = 200
numParticles = 50000
ticksPerFrame = 2
zmax = 300

fig = plt.figure()
ax = fig.add_subplot(111)

# meshgrid setup
x = y = np.linspace(1,gridSize,gridSize)
X, Y = np.meshgrid(x, y)

# colour map
vmin, vmax = 0, zmax
norm = colors.Normalize(vmin=vmin, vmax=vmax)

# Initialise all particles to the centre
locations = np.ones((numParticles, 2), dtype=int) * gridSize//2

for j in range(maxIterations):
    # randomly move particles
    locations += np.random.randint(-1, 2, locations.shape)

    if not (j+1) % ticksPerFrame:
        # Create and update new grid
        grid = np.zeros((gridSize, gridSize))

        for i in range(numParticles):
            x, y = locations[i]
            # check if particle is still on grid, then add it
            if ( 0 <= x < gridSize and 0 <= y < gridSize):
                grid[x, y] += 1

        print(j+1, '/', maxIterations)

        # clear previous plot and replot
        ax.clear()
        ax.scatter(X, Y, grid)

        #save to files
        plt.savefig('plots/sim-{:03d}.png'.format(j//ticksPerFrame))
