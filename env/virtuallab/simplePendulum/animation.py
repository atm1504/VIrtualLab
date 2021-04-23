import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation


class simplePendulum:
    def __init__(self, length=1, mass=0.1, damp=0.05, left=0, right=5):
        # Pass the input parameters
        self.b = damp  # 0.05
        self.g = 9.81
        self.l = length  # 1
        self.m = mass  # 0.1
        self.theta_0 = [left, right]  # Initial angle
        self.t = np.linspace(0, 20, 250)
        # solving ODE by function call
        self.theta = odeint(self.mode1, self.theta_0, self.t,
                            args=(self.b, self.g, self.l, self.m))

    def mode1(self, theta, t, b, g, l, m):
        theta1 = theta[0]
        theta2 = theta[1]
        dtheta1_dt = theta2
        dtheta2_dt = -(b/m)*theta2 - (g/l)*math.sin(theta1)
        dtheta_dt = [dtheta1_dt, dtheta2_dt]
        return dtheta_dt

    def show(self):
        fig = plt.figure(figsize=(5, 5), facecolor='w')
        ax = fig.add_subplot(1, 1, 1)
        plt.rcParams['font.size'] = 15
        lns = []

        for i in range(len(self.theta)):
            # plotting the string/chord
            ln, = ax.plot([0, np.sin(self.theta[i, 0])], [
                0, -np.cos(self.theta[i, 0])], color='k', lw=2)
        # plotting the bob
            bob, = ax.plot(
                np.sin(self.theta[i, 0]), -np.cos(self.theta[i, 0]), 'o', markersize=20, color='r')

            tm = ax.text(-0.9, 0.25, 'Time = %.1fs' % self.t[i])
            lns.append([ln, bob, tm])

        ax.set_aspect('equal', 'datalim')
        # saving the animation
        ani = animation.ArtistAnimation(fig, lns, interval=50)
        plt.show()


# plotting results for transient behavior
# plt.figure()
# plt.plot(t, theta[:, 0], 'b-', label=r'$frac{dtheta_1}{dt}=theta2$')
# plt.plot(t, theta[:, 1], 'r--',
#          label=r'$frac{dtheta_2}{dt}=frac{b}{m}theta_2-frac{g}{l}sintheta_1$')
# plt.ylabel('Plot')
# plt.xlabel('time')
# plt.legend(loc='best')
# plt.show()
# animation
simple = simplePendulum(1, 0.1, 0.05, 0, 5)
simple.show()
