from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib
import base64

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
