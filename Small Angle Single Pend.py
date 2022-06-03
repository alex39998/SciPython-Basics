import matplotlib.pyplot as plt
import matplotlib.animation as mtA
import numpy as np

#For a simple pendulumn: theta = theta_0 * cos (sqrt(g/L)t) | W=sqrt(g/L)

#Pendulumn initial condiiton in radians
theta_i=0.2
length=5
x0=length*np.sin(theta_i)
y0=length*np.cos(theta_i)

#Problem setup
nsteps = 20000
t_init = 0.0
t_final = 200.0
t = np.linspace(t_init, t_final, nsteps)
timeStep= t[1]-t[0]
theta=xA=yA=xN=yN=np.empty(nsteps,dtype=float)

#Numerical Sim
C=9.8/length #-g/l in the diffeq
ndEqs=2
h = np.zeros((ndEqs,nsteps), dtype=float)
#row 0 = angular position; row 1=angular velocity
#Define initial conditions
#x(0)=
h[0,0]=theta_i
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

def velocity_Verlet ():
    i=h
    for index in range(1,nsteps):
        h0Prev=i[0,index-1]
        h1Prev=i[1,index-1]
        vh= h1Prev - 0.5*C*np.sin(h0Prev)*timeStep
        #position
        i[0,index]=h0Prev + vh*timeStep
        #vel
        i[1,index]=vh - 0.5*C*np.sin(i[0,index])*timeStep*C
    return i

def thetaNToX(i):
    i = np.sin(h[0,:])*length
    return i
def thetaNToY(j):
    j = 10 - np.cos(h[0,:])*length
    return j

def thetaToX(i):
    i = np.sin(theta)*length
    return i
def thetaToY(j):
    j = 10 - np.cos(theta)*length
    return j

def main ():
    fig, ax = plt.subplots()
    ax.set_title("Pendulumn", fontsize=18)
    ax.set_xlim([-5,11])
    ax.set_ylim([0,15])

    anchor=[0,10]
    pendBall,=plt.plot(0,10-length,'bo',markersize=18, label='Analytical')
    pendBallNum,=plt.plot(0,10-length,'ro',markersize=18,alpha=0.5,label='Numerical')
    line,=plt.plot([anchor[0],0],[anchor[1],5],'b')
    lineNum,=plt.plot([anchor[0],0],[anchor[1],5],'r',alpha=0.5)
    xA[0]=x0
    yA[0]=y0

    #Analytical
    for index in range(0,np.size(theta)):
        theta[index]=theta_i*np.cos(np.sqrt(9.8/length)*t[index])
    xX = thetaToX(xA)
    yY = thetaToY(yA)

    #Numerical
    #EulerSys()
    velocity_Verlet()
    xnum = thetaNToX(xN)
    ynum = thetaNToY(yN)

    def animate(i):
        if (i>=np.size(xX)):
            return pendBall,line,pendBallNum,lineNum

        pendBall.set_data(xX[i],yY[i])
        line.set_data([anchor[0],xX[i]],[anchor[1],yY[i]])
        pendBallNum.set_data(xnum[i],ynum[i])
        lineNum.set_data([anchor[0],xnum[i]],[anchor[1],ynum[i]])
        return pendBall,line,pendBallNum,lineNum

    ani=mtA.FuncAnimation(fig,animate,interval=0.1,blit=True)
    leg=ax.legend()
    #ani.save('Single Pendulumn Small Angle.gif')
    plt.show()


if __name__ == '__main__':
    main()
