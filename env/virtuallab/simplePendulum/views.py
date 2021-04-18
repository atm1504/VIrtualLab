from django.shortcuts import render


def view_simple_pendulum(req):
    template = "simplePendulum/view.html"
    context = {
        "home": False,
        "simple": True,
        "double": False,
        "about": False
    }

    return render(req, template, context)


def view_simple_pendulum_code(req):
    template = "simplePendulum/code.html"
    context = {
        "home": False,
        "simple": True,
        "double": False,
        "about": False
    }
    return render(req, template, context)


def view_simple_simulation_setup(req):
    template = "simplePendulum/simulate.html"
    context = {
        "home": False,
        "simple": True,
        "double": False,
        "about": False
    }
    return render(req, template, context)
