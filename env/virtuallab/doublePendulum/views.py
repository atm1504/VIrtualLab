from django.shortcuts import render


def view_double_pendulum(req):
    template = "doublePendulum/view.html"
    context = {
        "home": False,
        "simple": False,
        "double": True,
        "about": False
    }
    return render(req, template, context)


def view_double_pendulum_code(req):
    template = "doublePendulum/code.html"
    context = {
        "home": False,
        "simple": False,
        "double": True,
        "about": False
    }
    return render(req, template, context)


def view_double_simulation_setup(req):
    template = "doublePendulum/simulate.html"
    context = {
        "home": False,
        "simple": False,
        "double": True,
        "about": False
    }
    return render(req, template, context)
