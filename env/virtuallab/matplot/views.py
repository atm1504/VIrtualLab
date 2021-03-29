from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib
import base64

import numpy as np
from matplotlib import animation


# Create your views here.


def showplot(req):
    template = "plot.html"
    plt.plot(range(10))
    fig = plt.gcf()
    # convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(req, template, {'data': uri})


def showanimePlot(req):
    # --------------------------Anime code
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        x = np.linspace(0, 2, 1000)
        y = np.sin(2 * np.pi * (x - 0.01 * i))
        line.set_data(x, y)
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=200, interval=20, blit=True)

    print(type(anim))
    plt.show()
    template = "anime.html"
    return render(req, template, {})
