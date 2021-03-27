from django.shortcuts import render

def view_simple_pendulum(req):
    template = "simplePendulum/view.html"

    return render(req,template, {})