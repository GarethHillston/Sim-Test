import matplotlib.pyplot as plt


def replot(shading, output_folder, iteration, locations):
    figure = plt.figure()
    axes = figure.add_subplot(111)
    image = axes.pcolormesh(locations, cmap=plt.get_cmap('inferno'), shading=shading, vmin=0, vmax=1)
    figure.colorbar(image, ax=axes)
    plt.savefig('{outputFolder}/sim-{iter:03d}.png'.format(outputFolder=output_folder, iter=iteration))
    plt.close()


class Plotting:
    pass
