from django.shortcuts import render


def view_double_pendulum(req):
    template = "doublePendulum/view.html"
    context = {
        "home": False,
        "simple": False,
        "double": True,
        "about":False
    }
    return render(req, template, context)
