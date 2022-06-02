import matplotlib.pyplot as plt
import matplotlib.animation as mtA
import numpy as np

#For a simple pendulumn: theta = theta_0 * cos (sqrt(g/L)t) | W=sqrt(g/L)


#For a mass-spring system, ma=-kx | mx''=-kx
#a=dv/dt, v=dx/dt
#Rewrite as a system of equations
#dv/dt=-k/m*x || dx/dt=v

# Derivative of function | dy/dx =f(x,y)
# dy
def deriv(a, b):
    return 1/10*(np.cos(a)*10+ np.sin(a))*np.exp(a/10)

#Pendulumn initial condiiton in degrees
theta_i=10
length=5
x0=length*np.sin(np.radians(theta_i))
y0=10-length+length*np.cos(np.radians(theta_i))


C=1 #h=k/m
ndEqs=2
nsteps = 6000
t_init = 0.0
t_final = 40.0
t = np.linspace(t_init, t_final, nsteps)
timeStep= t[1]-t[0]
h = np.zeros((ndEqs,nsteps), dtype=float)
#row 0 = position; row 1=velocity

theta=xA=yA=xN=yN=np.empty(nsteps,dtype=float)

def thetaToX(i):
    for index in range (1,theta.size):
        i[index]=np.sin(theta[index])*length
    return i
def thetaToY(j):
    for index in range (1,theta.size):
        j[index]=10-length+np.cos(theta[index])*length
    return j

def main ():
    fig, ax = plt.subplots()
    ax.set_title("Pendulumn", fontsize=18)
    ax.set_xlim([-5,11])
    ax.set_ylim([0,15])

    anchor=[0,10]
    pendBall,=plt.plot(0,10-length,'bo',markersize=20)
    line,=plt.plot([anchor[0],0],[anchor[1],5],'b')
    #plt.pause(2)
    xA[0]=x0
    yA[0]=y0

    #Analytical
    for index in range(0,theta.size):
        theta[index]=np.radians(theta_i)*np.cos(np.sqrt(9.8/length)*t[index])

    thetaToX(xA)
    thetaToY(yA)
    def animate(i):
        pendBall.set_data(xA[i],yA[i])

        line.set_data([anchor[0],xA[i]],[anchor[1],yA[i]])
        return pendBall, line

    ani=mtA.FuncAnimation(fig,animate,interval=1,blit=True)
    plt.show()

if __name__ == '__main__':
    main()



#Define initial conditions
#x(0)=
h[0,0]=3
#v(0)=
h[1,0]=0
def EulerSys ():
    for index in range(1,nsteps):
        h0Prev=h[0,index-1]
        h1Prev=h[1,index-1]
        #position
        h[0,index]=h0Prev + h1Prev*timeStep
        #vel
        h[1,index]=h1Prev - h0Prev*timeStep*C
    return h

 #def Ifig():
        #ax.set_title("Undampened Mass-Spring x(t)", fontsize=18)
        #ax.set_xlabel("Time", fontsize=14)
        #ax.set_ylabel("Position", fontsize=14)

    # Analytical plot
    #yAcc = h[0, 0] * np.cos(x * C)
    #line, = ax.plot(x, yAcc, "k", label='Analytical', alpha=0.8)
    #EulerSys plot position
    #EulerSys()
    #ax.plot(x, h[0,:], "r--", label='Euler', alpha=0.6)

    #def animate(i):
        #ax.plot(x[0:(i)], h[0, 0:(i)], "r--", label='Euler', alpha=0.6)

    #ani=mtA.FuncAnimation(fig,animate,init_func=Ifig, frames=10000,interval=1)
    #leg = ax.legend()