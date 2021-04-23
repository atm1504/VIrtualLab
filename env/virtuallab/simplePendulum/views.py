from django.shortcuts import render
from .forms import SimplePendulumForm
from .animation import run_simple_pendulum_animation


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
    simulationForm = SimplePendulumForm(req.POST or None)
    template = "simplePendulum/simulate.html"
    context = {
        "home": False,
        "simple": True,
        "double": False,
        "about": False,
        "form": simulationForm
    }
    if req.POST:
        run_simple_pendulum_animation()
    return render(req, template, context)
