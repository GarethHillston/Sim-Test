import numpy as np

import initialise_grid
import plot_data
import spread_model

grid_size = 100
max_iterations = 100


# Initialise cells
#locations = np.zeros((gridSize, gridSize), dtype=float)
locations = np.zeros((grid_size, grid_size), dtype=int)

initialise_grid.random_start(locations, grid_size, 5)

for i in range(max_iterations):
    plot_data.replot(locations, i)

    locations = spread_model.markov_basic(locations, grid_size)

plot_data.replot(locations, max_iterations + 1)
