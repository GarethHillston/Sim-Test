def spread_basic_threshold(locations, grid_size, infectious_threshold, virality):
    new_locs = locations.copy()

    # for each live cell, spread to neighbouring dead cells
    for x in range(grid_size):
        for y in range(grid_size):
            if locations[x, y] >= infectious_threshold:
                spill_over = locations[x, y] * virality
                x_start, x_stop = max(x - 1, 0), min(x + 1, grid_size)
                y_start, y_stop = max(y - 1, 0), min(y + 1, grid_size)
                new_locs[x_start, y] = min(locations[x_start, y] + spill_over, 1)
                new_locs[x_stop, y] = min(locations[x_stop, y] + spill_over, 1)
                new_locs[x, y_start] = min(locations[x, y_start] + spill_over, 1)
                new_locs[x, y_stop] = min(locations[x, y_stop] + spill_over, 1)
    return new_locs


def spread_basic(locations, grid_size, virality):
    new_locs = locations.copy()

    # for each live cell, spread to neighbouring dead cells
    for x in range(grid_size):
        for y in range(grid_size):
            if locations[x, y] >= 1:
                x_start, x_stop = max(x - 1, 0), min(x + 1, grid_size)
                y_start, y_stop = max(y - 1, 0), min(y + 1, grid_size)
                new_locs[x_start, y] += min(new_locs[x_start, y] + virality, 1)
                new_locs[x_stop, y] += min(new_locs[x_stop, y] + virality, 1)
                new_locs[x, y_start] += min(new_locs[x, y_start] + virality, 1)
                new_locs[x, y_stop] += min(new_locs[x, y_stop] + virality, 1)
    return new_locs


class SpreadModels:
    pass
