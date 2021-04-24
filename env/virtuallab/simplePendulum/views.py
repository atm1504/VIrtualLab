from django.shortcuts import render
from .forms import SimplePendulumForm
from .animation import run_simple_pendulum_animation
from virtuallab.utils import isNumber


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
        # Extract the datas
        mass_of_bob_in_kg = req.POST.get("mass_of_bob_in_kg")
        length_of_string_in_m = req.POST.get("length_of_string_in_m")
        damping_factor = req.POST.get("damping_factor")
        theta0_left_value = req.POST.get("theta0_left_value")
        theta0_right_value = req.POST.get("theta0_right_value")

        # Check for data validity
        if isNumber(mass_of_bob_in_kg) and isNumber(length_of_string_in_m) and isNumber(damping_factor) and isNumber(theta0_left_value) and isNumber(theta0_right_value):
            mass_of_bob_in_kg = float(mass_of_bob_in_kg)
            length_of_string_in_m = float(length_of_string_in_m)
            damping_factor = float(damping_factor)
            theta0_left_value = float(theta0_left_value)
            theta0_right_value = float(theta0_right_value)
        else:
            print("Else")

        run_simple_pendulum_animation(length=length_of_string_in_m, mass=mass_of_bob_in_kg,
                                      damp=damping_factor, left=theta0_left_value, right=theta0_right_value)
    return render(req, template, context)
