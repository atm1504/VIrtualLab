
from django.conf.urls import url
from django.urls import path

from .views import view_simple_pendulum, view_simple_pendulum_code, view_simple_simulation_setup

urlpatterns = [
    path("", view_simple_pendulum, name="simple_pendulum_view"),
    path("code/", view_simple_pendulum_code, name="simple_pendulum_code"),
    path("simulate/", view_simple_simulation_setup,
         name="simple_pendulum_simulate"),
]
