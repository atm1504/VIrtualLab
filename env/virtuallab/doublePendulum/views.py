from django.shortcuts import render
from .forms import DoublePendulumForm
from .animation import run_double_pendulum_animation
from virtuallab.utils import RepresentsNumber


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
    simulationForm = DoublePendulumForm(req.POST or None)

    template = "doublePendulum/simulate.html"
    context = {
        "home": False,
        "simple": False,
        "double": True,
        "about": False,
        "form": simulationForm
    }
    if req.POST:
        # Extract data from the form
        length1 = req.POST.get("length_of_first_string_in_m")
        length2 = req.POST.get("length_of_second_string_in_m")
        mass1 = req.POST.get("mass_of_first_bob_in_kg")
        mass2 = req.POST.get("mass_of_second_bob_in_kg")

        if RepresentsNumber(length1) and RepresentsNumber(length2) and RepresentsNumber(mass1) and RepresentsNumber(mass2):
            length1 = float(length1)
            length2 = float(length2)
            mass2 = float(mass2)
            mass1 = float(mass1)
        else:
            print("else executed")

        # call the show pendulum option
        run_double_pendulum_animation(
            length1=length1, length2=length2, mass1=mass1, mass2=mass2)
    return render(req, template, context)
