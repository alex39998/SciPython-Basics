import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as mtA
import numpy as np
import math

# Derivative of function | dy/dx =
def deriv(a, b):
    return 1/10*(np.cos(a)*10+ np.sin(a))*np.exp(a/10)

nsteps = 1000
t_init = 0.0
t_final = 20.0
x = np.linspace(t_init, t_final, nsteps)
timeStep= x[1]-x[0]
yInit=0
yEul = yMid = yRuK = np.empty(nsteps, dtype=float)
yEul[0] = yMid[0] = yRuK[0] = yInit

def Euler ():
    for index in range(1,nsteps):
        yPrev=yEul[index-1]
        yEul[index]=deriv(x[index], yPrev)*timeStep + yPrev
    return yEul

def Midpoint ():
    for index in range(1,nsteps):
        yPrev=yMid[index-1]
        yHalf=deriv(x[index], yPrev)*timeStep + yPrev
        yMid[index]=deriv((x[index]+timeStep/2), yHalf)*timeStep + yPrev
    return yMid

def Runge_Kutta ():
    for index in range(1, nsteps):
        yPrev = yRuK[index - 1]
        k1 = deriv(x[index], yPrev)*timeStep
        k2 = deriv((x[index] + timeStep/2), (yPrev + k1/2))*timeStep
        k3 = deriv((x[index] + timeStep/2), (yPrev + k2/2))*timeStep
        k4 = deriv((x[index] + timeStep), (yPrev+k3))*timeStep
        yRuK[index] = k1 / 6 + k2 / 3 + k3 / 3 + k4 / 6 + yPrev
    return yRuK

def main ():
    fig, ax = plt.subplots()
    # Analytical plot
    yAcc = np.sin(x)*np.exp(x/10)
    ax.plot(x, yAcc, "k", label='Analytical')

    # Euler plot
    Euler()
    ax.plot(x, yEul, "r--", label='Euler')
    # Midpoint plot
    Midpoint()
    ax.plot(x, yMid, "g--", label='Midpoint')
    # Runge-Kutta plot
    Runge_Kutta()
    ax.plot(x, yRuK, "b--", label='RuKt')
    leg = ax.legend()
    plt.show()

if __name__ == '__main__':
    main()


