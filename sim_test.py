import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import  colors

gridSize = 50
maxIterations = 200
numParticles = 50000
ticksPerFrame = 2
zmax = 300

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

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
        ax.plot_surface(
            X, Y, grid,
            rstride = 1,
            cstride = 1,
            cmap = plt.cm.autumn,
            linewidth = 1,
            vmin = vmin,
            vmax = vmax,
            norm = norm)
        ax.set_zlim(0, zmax)

        #save to files
        plt.savefig('diff-{:03d}.png'.format(j//ticksPerFrame))
