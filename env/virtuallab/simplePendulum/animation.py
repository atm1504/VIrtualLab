import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation


def mode1(theta, t, b, g, l, m):
    theta1 = theta[0]
    theta2 = theta[1]
    dtheta1_dt = theta2
    dtheta2_dt = -(b/m)*theta2 - (g/l)*math.sin(theta1)
    dtheta_dt = [dtheta1_dt, dtheta2_dt]
    return dtheta_dt


# Initializing important parameters
# damping coefficient
b = 0.05
g = 9.81
l = 1
m = 0.1
theta_0 = [0, 5]
t = np.linspace(0, 100, 1500)
# solving ODE by function call
theta = odeint(mode1, theta_0, t, args=(b, g, l, m))

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

fig = plt.figure(figsize=(5, 5), facecolor='w')
ax = fig.add_subplot(1, 1, 1)
plt.rcParams['font.size'] = 15
lns = []

for i in range(len(theta)):
    # plotting the string/chord
    ln, = ax.plot([0, np.sin(theta[i, 0])], [
                  0, -np.cos(theta[i, 0])], color='k', lw=2)
 # plotting the bob
    bob, = ax.plot(
        np.sin(theta[i, 0]), -np.cos(theta[i, 0]), 'o', markersize=20, color='r')

    tm = ax.text(-0.9, 0.25, 'Time = %.1fs' % t[i])
    lns.append([ln, bob, tm])

ax.set_aspect('equal', 'datalim')
# saving the animation
ani = animation.ArtistAnimation(fig, lns, interval=50)
plt.show()
