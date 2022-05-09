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

fig,ax=plt.subplots()
y=np.sin(t)
ax.plot(t,y)

val=np.empty(rectangles+1)
ts=np.empty(rectangles+1)
tp=np.empty(rectangles+1)
for i in range (1,rectangles+1):
    val[i]=np.sin(t_init + interval*i)
    ts[i]=t_init+interval*i
    tp[i]=t_init+interval*(i-1)

ax.fill_betweenx(val, tp, ts, step='post') #where = None

plt.show()


