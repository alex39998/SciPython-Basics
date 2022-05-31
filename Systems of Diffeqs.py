import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as mtA
import numpy as np
import math

#For a mass-spring system, ma=-kx | mx''=-kx
#a=dv/dt, v=dx/dt
#Rewrite as a system of equations
#dv/dt=-k/m*x || dx/dt=v

# Derivative of function | dy/dx =f(x,y)
# dy
def deriv(a, b):
    return 1/10*(np.cos(a)*10+ np.sin(a))*np.exp(a/10)

C=1 #h=k/m
ndEqs=2
nsteps = 6000
t_init = 0.0
t_final = 40.0
x = np.linspace(t_init, t_final, nsteps)
timeStep= x[1]-x[0]
h = np.zeros((ndEqs,nsteps), dtype=float)
#row 0 = position; row 1=velocity

#Define initial conditions
#x(0)=
h[0,0]=3
#v(0)=
h[1,0]=0

yEul = yRuK = np.empty(nsteps, dtype=float)

def EulerSys ():
    for index in range(1,nsteps):
        h0Prev=h[0,index-1]
        h1Prev=h[1,index-1]
        #position
        h[0,index]=h0Prev + h1Prev*timeStep
        #vel
        h[1,index]=h1Prev - h0Prev*timeStep*C
    return h


def main ():
    fig, ax = plt.subplots()
    #line,=ax.plot([],[])
    def Ifig():
        ax.set_title("Undampened Mass-Spring x(t)", fontsize=18)
        ax.set_xlabel("Time", fontsize=14)
        ax.set_ylabel("Position", fontsize=14)
        # Analytical plot
        yAcc = h[0, 0] * np.cos(x * C)
        line, = ax.plot(x, yAcc, "k", label='Analytical', alpha=0.8)

    #EulerSys plot position
    EulerSys()
    #ax.plot(x, h[0,:], "r--", label='Euler', alpha=0.6)

    def animate(i):
        ax.plot(x[0:(i)], h[0, 0:(i)], "r--", label='Euler', alpha=0.6)

    ani=mtA.FuncAnimation(fig,animate,init_func=Ifig(), frames=10000,interval=1)
    leg = ax.legend()
    plt.show()

if __name__ == '__main__':
    main()





def Runge_Kutta ():
    for index in range(1, nsteps):
        yPrev = yRuK[index - 1]
        k1 = deriv(x[index], yPrev)*timeStep
        k2 = deriv((x[index] + timeStep/2), (yPrev + k1/2))*timeStep
        k3 = deriv((x[index] + timeStep/2), (yPrev + k2/2))*timeStep
        k4 = deriv((x[index] + timeStep), (yPrev+k3))*timeStep
        yRuK[index] = k1 / 6 + k2 / 3 + k3 / 3 + k4 / 6 + yPrev

        h0Prev = h[0, index - 1]
        h1Prev = h[1, index - 1]

    return yRuK