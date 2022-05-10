import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as mtA
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

nsteps = 10000
t_init = 0.0
t_final = 20.0
t=np.linspace(t_init,t_final, nsteps)

rectangles=30
val = np.empty(rectangles + 1)
ts = np.empty(rectangles + 1)
tp = np.empty(rectangles + 1)

def fill_between_3d(ax, x1, y1, z1, x2, y2, z2, mode=1, c='steelblue', alpha=0.6):
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
    pass

def main ():
    fig =plt.figure()
    ax=fig.add_subplot(projection='3d')
    #line, = ax.plot([], [], [])
    ax.plot(x_param(),y_param(),z_param())

    set01xtoline = [x_param(), y_param(), np.zeros(len(t))]
    set1 = [x_param(), y_param(), z_param()]
    def animate(i):
        s01xtl = set01xtoline[0:(i-1), 0:(i-1), 0:(i-1)]
        s1 = set1[0:(i-1), 0:(i-1), 0:(i-1)]
        p = fill_between_3d(ax, *s01xtl, *s1, mode=1, c="C0")

    ani = mtA.FuncAnimation(fig,animate, frames=1000, interval=5)
    #fill_between_3d(ax, *set01xtoline, *set1, mode=1, c="C0")
    plt.show()

if __name__ == '__main__':
    main()