
from django.conf.urls import url
from django.urls import path

from .views import view_double_pendulum, view_double_pendulum_code, view_double_simulation_setup

urlpatterns = [
    path("", view_double_pendulum, name="double_pendulum_view"),
    path("code/", view_double_pendulum_code, name="double_pendulum_code"),
    path("simulate/", view_double_simulation_setup,
         name="double_pendulum_simulate"),
]
