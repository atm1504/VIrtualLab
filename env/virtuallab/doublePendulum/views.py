from django.shortcuts import render

def view_double_pendulum(req):
    template = "doublePendulum/view.html"
    return render(req,template, {})
