
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
y=np.sin(t)

rectangles=30
interval=(t_final-t_init)/rectangles


#parameterization of curve
def x_param ():
    x=np.cos(t)
    return x

def y_param ():
    y = np.sin(t)
    return y

def z_param ():
    z=np.sqrt(t)
    return z

def reinman ():
    #Loop through  from start point to end point
    #Interval = (end-start)/rectangles
    #Given a parametric x=x(t) and y=y(t)
    #x_n = x_n(start + interval*n)
    #y_n=y_n(start + interval*n)
    #Every rectangle:
    #plt.fill_between_3d()

    
    #for h in range(0,interval):

        #return
    pass

def main ():
    fig =plt.figure()
    ax=fig.add_subplot(projection='3d')
    ax.plot(x_param(),y_param(),z_param())

    

    plt.show()

if __name__ == '__main__':
    main()
