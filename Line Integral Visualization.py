
import matplotlib.patches as mpatches
import matplotlib.animation as mtA
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

nsteps = 10000
t_init = 0.0
t_final = 20.0
t=np.linspace(t_init,t_final, nsteps)

rectangles=30
val = np.empty(rectangles + 1)
ts = np.empty(rectangles + 1)
tp = np.empty(rectangles + 1)

def fill_between_3d(ax, x1, y1, z1, x2, y2, z2, mode=1, c='steelblue', alpha=0.5):
    if mode == 1:

        for i in range(len(x1) - 1):
            verts = [(x1[i], y1[i], z1[i]), (x1[i + 1], y1[i + 1], z1[i + 1])] + \
                    [(x2[i + 1], y2[i + 1], z2[i + 1]), (x2[i], y2[i], z2[i])]

            ax.add_collection3d(Poly3DCollection([verts],
                                                 alpha=alpha,
                                                 linewidths=0,
                                                 color=c))

    if mode == 2:
        verts = [(x1[i], y1[i], z1[i]) for i in range(len(x1))] + \
                [(x2[i], y2[i], z2[i]) for i in range(len(x2))]

        ax.add_collection3d(Poly3DCollection([verts], alpha=alpha, color=c))

#parameterization of curve
def x_param ():
    x=np.cos(t)
    return x

def y_param ():
    y = np.sqrt(t)
    return y

def z_param ():
    z=t
    return z

def reinman ():
    #interval = (t_final - t_init) / rectangles

    """for i in range(1, rectangles + 1):
        val[i] = np.sin(t_init + interval * i)
        ts[i] = t_init + interval * i
        tp[i] = t_init + interval * (i - 1)"""
    pass

def fillintegral():
    #set01xtoline = [np.zeroes(len(x)), y_param(), np.zeroes(len(x)]
    #set1 = [np.zeroes(len(x)), y_param(), z_param()]
    #fill_between_3d(ax, *set01xtoline, *set1, mode=1, c="C0")
    pass

def main ():
    fig =plt.figure()
    ax=fig.add_subplot(projection='3d')
    ax.plot(x_param(),y_param(),z_param(), color="orange")

    #ax.fill_betweenx(val, tp, ts, step='post')
    set01xtoline = [x_param(), y_param(), np.zeros(len(t))]
    set1 = [x_param(), y_param(), z_param()]
    fill_between_3d(ax, *set01xtoline, *set1, mode=1, c="C0")
    plt.show()

if __name__ == '__main__':
    main()


    """
    Function similar to the matplotlib.pyplot.fill_between function but 
    for 3D plots.
    input:
        ax -> The axis where the function will plot.

        x1 -> 1D array. x coordinates of the first line.
        y1 -> 1D array. y coordinates of the first line.
        z1 -> 1D array. z coordinates of the first line.

        x2 -> 1D array. x coordinates of the second line.
        y2 -> 1D array. y coordinates of the second line.
        z2 -> 1D array. z coordinates of the second line.
    modes:
        mode = 1 -> Fill between the lines using the shortest distance between 
                    both. Makes a lot of single trapezoids in the diagonals 
                    between lines and then adds them into a single collection.
        mode = 2 -> Uses the lines as the edges of one only 3d polygon.

    Other parameters (for matplotlib): 
        c -> the color of the polygon collection.
        alpha -> transparency of the polygon collection.
    """
