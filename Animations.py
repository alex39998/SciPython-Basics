import matplotlib.pyplot as plt
import matplotlib.animation as mta
import numpy as np

#Make a dot moving along a line
#FuncAnimation (figure, function (to call), *bunch of other optional params)
#Modify specified figure with the function

nsteps = 100
t_init = 0.0
t_final = 20.0
x = np.linspace(t_init, t_final, nsteps)
timeStep= x[1]-x[0]
yInit=0
yAna = yEul = yMid = yRuK = np.empty(nsteps, dtype=float)
yAna[0] = yEul[0] = yMid[0] = yRuK[0] = yInit
i=0

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

def datagen ():
    #Define function, sorta
    for z in range (0,nsteps):
        yield t,y

def fig_I ():
    line.set_data([],[])
    ax.set_xlim(t_init,t_final)
    return line

def func_1(i):
    t=x[i]
    y=x[i]
    #Need to modularize this after I get it working
    line.set_data(t,y)
    return line,

def main():
    if i>nsteps-1:
        ani = mta.FuncAnimation(fig_I,func_1, init_func=figI)
    plt.show()

if __name__ == '__main__':
    main()

""" t_final=30
fig = plt.figure()
axis = plt.axes(xlim=(-1,t_final), ylim=(-1,t_final))

line,=axis.plot([],[])

def initial1():
    line.set_data([],[])
    return line,

def animate(i):
    x=np.linspace(0,t_final,1000)

    y=x[i]
    line.set_data(x,y)

    return line,

anim= mtA.FuncAnimation(fig, animate,init_func=initial1, frames=2,interval=20,blit=True)
plt.show()"""
