import matplotlib.pyplot as plt
import matplotlib.animation as mtA
import numpy as np

#Pendulumn initial condiiton in radians
theta_i=2
length=5
x0=length*np.sin(theta_i)
y0=length*np.cos(theta_i)
theta_i2=2
l2=5
x20=x0+l2*np.sin(theta_i2)
y20=y0+l2*np.cos(theta_i2)

#Problem setup
nsteps = 10000
t_init = 0.0
t_final = 200.0
t = np.linspace(t_init, t_final, nsteps)
timeStep= t[1]-t[0]
theta=xN2=yN2=xN=yN=np.empty(nsteps,dtype=float)

C=9.8/length #g/l
ndEqs=2
h = h2 = np.zeros((ndEqs,nsteps), dtype=float)

#row 0 = angular position; row 1=angular velocity
#Define initial conditions
h[0,0]=theta_i
h[1,0]=0

h2[0,0]=theta_i2
h2[1,0]=0

#Integrate equations of motion of double pend taken from wikipedia
def velV2 ():
    for index in range (1,nsteps):
        h0Prev = h[0, index - 1]
        h1Prev = h[1, index - 1]
        h02Prev = h2[0,index-1]
        h12Prev = h2[1,index-1]

        vh = h1Prev - 0.5*timeStep*0.5*length*length*(h1Prev*h12Prev*np.sin(h0Prev-h02Prev)+3*C*np.sin(h02Prev))
        h[0,index] = h0Prev + vh*timeStep
        h[1,index] = vh - 0.5*timeStep*0.5*length*length*(h[1,index]*h2[1,index]*np.sin(h[0,index]-h2[0,index])+3*C*np.sin(h2[0,index]))

        vh2 = h12Prev - 0.5*timeStep*0.5*l2*l2*(h1Prev*h12Prev*-1*np.sin(h0Prev-h02Prev)+C*np.sin(h02Prev))
        h2[0,index] = h02Prev + vh2*timeStep
        h2[1,index] = vh2 - 0.5*timeStep*0.5*l2*l2*(h[1,index]*h2[1,index]*-1*np.sin(h[0,index]-h2[0,index])+C*np.sin(h2[0,index]))
    return h,h2

#Convert theta1 array to x and y array respectively
def thetaNToX(i):
    i = np.sin(h[0,:])*length
    return i
def thetaNToY(j):
    j = 10 - np.cos(h[0,:])*length
    return j


def main ():
    fig, ax = plt.subplots()
    ax.set_title("Double Pendulumn", fontsize=18)
    ax.set_xlim([-10,10])
    ax.set_ylim([-2,15])

    anchor=[0,10]
    a2 = [x0,y0]
    pendBall1, = plt.plot(0, anchor[1] - length, 'ro', markersize=18)
    line1, = plt.plot([anchor[0], 0], [anchor[1], anchor[1]-length], 'r')
    pendBall2,=plt.plot(0,anchor[1]-length-l2,'ro',markersize=18)
    line2,=plt.plot([a2[0],0],[a2[1],10-length-l2],'b')

    #velocity_Verlet()
    velV2()
    xnum = thetaNToX(xN)
    ynum = thetaNToY(yN)

    def animate(i):
        if (i>=np.size(xnum)):
            return pendBall1,line1,pendBall2,line2

        a2 = [xnum[i], ynum[i]]
        xnum2 = a2[0] + np.sin(h2[0, i]) * length
        ynum2 = 10 - a2[1] - np.cos(h2[0, i]) * length

        pendBall1.set_data(xnum[i],ynum[i])
        line1.set_data([anchor[0],xnum[i]],[anchor[1],ynum[i]])

        pendBall2.set_data(xnum2, ynum2)
        line2.set_data([a2[0], xnum2], [a2[1], ynum2])
        return pendBall1,line1,pendBall2,line2

    ani=mtA.FuncAnimation(fig,animate,interval=0.8,blit=True)
    plt.show()

if __name__ == '__main__':
    main()