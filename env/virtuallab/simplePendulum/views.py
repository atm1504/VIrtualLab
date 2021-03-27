from django.shortcuts import render


def view_simple_pendulum(req):
    template = "simplePendulum/view.html"
    context = {
        "home": False,
        "simple": True,
        "double": False,
        "about":False
    }

    return render(req, template, context)
